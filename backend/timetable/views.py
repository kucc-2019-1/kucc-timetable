from rest_framework import viewsets

from . import models
from . import  serializers


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer


class Time_tableViewSet(viewsets.ModelViewSet):
    queryset = models.TimeTable.objects.all()
    serializer_class = serializers.TimeTableSerializer


class Time_indexViewSet(viewsets.ModelViewSet):
    queryset = models.TimeIndex.objects.all()
    serializer_class = serializers.TimeIndexSerializer