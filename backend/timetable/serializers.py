from rest_framework import serializers

from . import models


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'


class TimeTableViewSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)
    data = serializers.ListField()


class DateListSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)
    data = serializers.DictField()


class AvailableReservationTimeViewSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)
    data = serializers.ListField()


class TimeIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimeIndex
        fields = '__all__'
