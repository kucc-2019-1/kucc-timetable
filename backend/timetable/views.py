from rest_framework import viewsets, views, generics
from rest_framework.response import Response
from django.utils import timezone

from . import models
from . import serializers


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer


class TimeTableView(generics.ListAPIView):
    serializer_class = serializers.TimeTableViewSerializer

    def get_queryset(self):
        return models.Reservation.objects.all()


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

        data = [
            {
                "message": "",
                "data": {"day": str(timezone.now())[:10], "day_of_week": dayofweek(timezone.now().weekday())}
            }
        ]
        instance = serializers.DateListSerializer(data, many=True).data
        return Response(instance)


class Time_indexViewSet(viewsets.ModelViewSet):
    queryset = models.TimeIndex.objects.all()
    serializer_class = serializers.TimeIndexSerializer


# class AvailableReservationTime





