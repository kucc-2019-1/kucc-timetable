from rest_framework import viewsets, views, generics
from rest_framework.response import Response

from . import models
from . import serializers


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer


class TimeTableView(generics.ListAPIView):
    serializer_class = serializers.TimeTableViewSerializer

    def get_queryset(self):
        return models.Reservation.objects.all()


class Time_indexViewSet(viewsets.ModelViewSet):
    queryset = models.TimeIndex.objects.all()
    serializer_class = serializers.TimeIndexSerializer





