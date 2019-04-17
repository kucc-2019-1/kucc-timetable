from rest_framework import viewsets, views
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime

from . import models
from . import serializers


# 1. 날짜 목록 API(GET) /day
class TimeTableView(views.APIView):

    def get(self, request):
        data = []
        queryset = models.TimeTable.objects.filter(day__gte=timezone.now()).order_by('day', 'time_index')

        reservation = queryset[0].reservation
        title = reservation.title
        name = reservation.user.name
        day = (queryset[0].day-timezone.now().date()).days
        start_time = queryset[0].time_index.time_index_id
        end_time = queryset[0].time_index.time_index_id

        for model in queryset:
            if model.reservation == reservation:
                end_time = model.time_index.time_index_id

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

                reservation = model.reservation
                title = reservation.title
                name = reservation.user.name
                day = (model.day-timezone.now().date()).days
                start_time = model.time_index.time_index_id
                end_time = model.time_index.time_index_id

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


# 2. 날짜별 예약 가능 시간(GET) /times?day=2019-03-01
class AvailableReservationTimeView(views.APIView):
    def get(self, request):
        day = request.GET.get('day')
        day = datetime.strptime(day, '%Y-%m-%d').date()
        unavaiabletime = models.TimeTable.objects.filter(day=day)
        countindex = 9
        order = set([])
        for i in range(0, countindex):
            order.add(i)

        for model in unavaiabletime:
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


# 3. 예약 목록 보기(GET) /timetable
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




