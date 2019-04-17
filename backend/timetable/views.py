from rest_framework import viewsets, views, generics
from rest_framework.response import Response
from django.utils import timezone


from . import models
from . import serializers


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer


# class TimeTableView(generics.ListAPIView):
#     serializer_class = serializers.TimeTableViewSerializer
#
#     def get_queryset(self):
#         return models.Reservation.objects.all()


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


class Time_indexViewSet(viewsets.ModelViewSet):
    queryset = models.TimeIndex.objects.all()
    serializer_class = serializers.TimeIndexSerializer


# class AvailableReservationTime





