from django.db import models


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    user = models.ForeignKey('user.User', models.DO_NOTHING)

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = 'reservation'


class TimeIndex(models.Model):
    time_index_id = models.IntegerField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time)[0:5] + ' ~ ' + str(self.end_time)[0:5]

    class Meta:
        db_table = 'time_index'


class TimeTable(models.Model):
    time_table_id = models.AutoField(primary_key=True)
    day = models.DateField()
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING, blank=True, null=True)
    time_index = models.ForeignKey(TimeIndex, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.reservation) + ' ' + str(self.time_index)

    class Meta:
        db_table = 'time_slot'
