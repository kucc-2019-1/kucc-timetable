from rest_framework import serializers

from . import models


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimeTable
        fields = '__all__'


class TimeIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimeIndex
        fields = '__all__'
