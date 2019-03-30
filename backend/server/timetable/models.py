from django.db import models

class Reservation(models.Model):
    reservation_id = models.CharField(max_length=20)
    title = models.CharField(max_length=10)


class Time_index(models.Model):
    time = models.IntegerField()
    index = models.TimeField()


class Time_table(models.Model):
    reservation_id = models.CharField(max_length=20)
    day = models.DateField()
    time = models.ForeignKey(Time_index, on_delete=models.CASCADE)
