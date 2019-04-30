import json

from django.http import HttpResponse
from django.views import generic
from rest_framework import viewsets, views
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime, timedelta

from . import models
from . import serializers


# 1. 날짜 목록 API(GET) /day
class DateListView(views.APIView):

    def get(self, request):
        def dayofweek(args):
            if args == 0:
                return "SUN"
            elif args == 1:
                return "MON"
            elif args == 2:
                return "TUE"
            elif args == 3:
                return "WEN"
            elif args == 4:
                return "THI"
            elif args == 5:
                return "FRI"
            elif args == 6:
                return "SAT"

        dictionary = [
            {
                "message": "",
                "data": {"day": str(timezone.now().date()), "day_of_week": dayofweek(timezone.now().weekday())}
            }
        ]
        instance = serializers.DateListSerializer(dictionary, many=True).data
        return Response(instance)


# 2. 날짜별 예약 가능 시간(GET) /times?day=2019-03-01
class AvailableReservationTimeView(views.APIView):
    def get(self, request):
        day = request.GET.get('day' or None)

        try:
            day = datetime.strptime(day, '%Y-%m-%d').date()

            # 해당 날짜에 있는 예약들을 unavailable에 반환하는 쿼리
            unavailabletime = models.TimeTable.objects.filter(day=day)

            # timeIndex 테이블의 레코드 개수 저장 (지금은 인덱스를 9까지만 만들어서 나중에 바꿀 예정)
            countindex = 9

            # orderset을 만들어서 모든 인덱스를 저장
            order = set([])
            for i in range(0, countindex):
                order.add(i)

            # 이미 예약이 되어 있는 시간 제거
            for model in unavailabletime:
                order.remove(model.time_index.time_index_id)

            data = []

            for i in order:
                dict = {"order": i, "time": str(models.TimeIndex.objects.get(time_index_id=i))}
                data.append(dict)

            dictionary = [
                {
                    "message": "",
                    "data": data,
                }
            ]
            instance = serializers.AvailableReservationTimeViewSerializer(dictionary, many=True).data
            return Response(instance)

        # day 값이 없을 경우 예외처리
        except TypeError:
            dictionary = [
                {
                    "message": "day 값이 없어요",
                    "data": [],
                }
            ]
            instance = serializers.AvailableReservationTimeViewSerializer(dictionary, many=True).data
            return Response(status=400, data=instance)

        # day에 올바른 값이 오지 않았을 경우 예외처리
        except ValueError:
            dictionary = [
                {
                    "message": "day 값이 잘못되었어요",
                    "data": [],
                }
            ]
            instance = serializers.AvailableReservationTimeViewSerializer(dictionary, many=True).data
            return Response(instance)


# 3. 예약 목록 보기(GET) /timetable
class TimeTableView(views.APIView):
    def get(self, request):
        data = []



        # 우선 오늘 및 이후의 날짜의 데이터만 가져옴. 이 때 날짜순, time_index 순으로 정렬
        queryset = models.TimeTable.objects.filter(day__gte=timezone.now()).order_by('day', 'time_index')

        # 최초 데이터를 저장
        reservation = queryset[0].reservation
        title = reservation.title
        name = reservation.user.name
        day = (queryset[0].day-timezone.now().date()).days
        start_time = queryset[0].time_index.time_index_id
        end_time = queryset[0].time_index.time_index_id

        # for 문을 이용하여 직접값과 비교
        for model in queryset:

            # 같다면, 같은 예약이기 때문에 end_time만 바꾸어줌
            if model.reservation == reservation:
                end_time = model.time_index.time_index_id

            # 다르다면, 다른 예약이기 때문에 현재까지 저장된 데이터를 data에 append 시켜줌
            else:
                data.append(
                    {
                        "title": title,
                        "name": name,
                        "day": day,
                        "start_time": start_time,
                        "end_time": end_time
                    }
                )

            # 그리고 다시 초기화
                reservation = model.reservation
                title = reservation.title
                name = reservation.user.name
                day = (model.day-timezone.now().date()).days
                start_time = model.time_index.time_index_id
                end_time = model.time_index.time_index_id

        # for 문이 끝나고 마지막 남은 데이터까지 처리
        data.append(
            {
                "title": title,
                "name": name,
                "day": day,
                "start_time": start_time,
                "end_time": end_time
            }
        )

        dictionary = [
            {
                "message": "",
                "data": data,
            }
        ]
        instance = serializers.TimeTableViewSerializer(dictionary, many=True).data
        return Response(instance)


# 4. 예약 만들기(POST) /reservation
class MakeReservation(views.APIView):

    def post(self, request):
        user = request.user

        # json 데이터를 받음
        title = request.data["title"]
        day = timezone.now() + timedelta(days=request.data["day"])
        start_time = request.data["start_time"]
        end_time = request.data["end_time"]

        # 해당 날짜에 있는 예약들을 반환하는 쿼리
        unavailabletime = models.TimeTable.objects.filter(day=day)

        # order에 이제 들어갈 예약의 모든 time_index를 넣어줌
        order = set([])
        for i in range(start_time, end_time+1):
            order.add(i)
        ordersize = len(order)

        # 위에서 구한 unavailabletime와 겹치는 부분이 있으면 제거해줌
        for model in unavailabletime:
            order.remove(model.time_index.time_index_id)
        ordersizecmp = len(order)

        # 두 값이 다르다는 것은, 겹치는 시간이 발생하였다는 뜻이기 때문에, 두 값을 같을 경우에만 실행
        if ordersize == ordersizecmp:
            reservationmodel = models.Reservation(title=title, user=user)
            reservationmodel.save()

            for index in range(start_time, end_time+1):
                timetablemodel = models.TimeTable(
                    day=day,
                    reservation=reservationmodel,
                    time_index=models.TimeIndex.objects.get(time_index_id=index)
                )
                timetablemodel.save()
            return Response(data={"message": ""})
        else:
            return Response(status=400, data={"message": "이미 예약된 시간입니다."})




