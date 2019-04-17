from rest_framework import serializers

from . import models


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'


# class TimeTableViewSerializer(serializers.ModelSerializer):
#     name = serializers.SerializerMethodField(read_only=True)
#     day = serializers.SerializerMethodField(read_only=True)
#     start_time = serializers.SerializerMethodField(read_only=True)
#     end_time = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = models.Reservation
#         fields = [
#             'title',
#             'name',
#             'day',
#             'start_time',
#             'end_time',
#         ]
#
#     def get_name(self, obj):
#         return obj.catch_name()
#
#     def get_day(self, obj):
#         return obj.catch_day()
#
#     def get_start_time(self, obj):
#         return str(obj.catch_time()['start_time'])[0:5]
#
#     def get_end_time(self, obj):
#         return str(obj.catch_time()['end_time'])[0:5]


class TimeTableViewSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)
    data = serializers.ListField()



class DateListSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)
    data = serializers.DictField()




class TimeIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimeIndex
        fields = '__all__'
