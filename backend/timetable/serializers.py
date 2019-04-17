from rest_framework import serializers


# 1. 날짜 목록 API(GET) /day
class DateListSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)
    data = serializers.DictField()


# 2. 날짜별 예약 가능 시간(GET) /times?day=2019-03-01
class AvailableReservationTimeViewSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)
    data = serializers.ListField()


# 3. 예약 목록 보기(GET) /timetable
class TimeTableViewSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)
    data = serializers.ListField()