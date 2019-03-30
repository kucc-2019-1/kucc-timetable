from rest_framework import viewsets

from . import models
from . import  serializers


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer


class Time_tableViewSet(viewsets.ModelViewSet):
    queryset = models.Time_table.objects.all()
    serializer_class = serializers.Time_TableSerializer


class Time_indexViewSet(viewsets.ModelViewSet):
    queryset = models.Time_index.objects.all()
    serializer_class = serializers.Time_IndexSerializer