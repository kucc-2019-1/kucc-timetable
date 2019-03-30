from rest_framework import serializers

from . import models


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'


class Time_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Time_table
        fields = '__all__'


class Time_IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Time_index
        fields = '__all__'