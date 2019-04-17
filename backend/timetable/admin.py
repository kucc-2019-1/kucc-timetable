from django.contrib import admin

from .models import Reservation, TimeIndex, TimeTable


class TimeTableInline(admin.StackedInline):
    model = TimeTable
    extra = 15


class ReservationAdmin(admin.ModelAdmin):
    inlines = [TimeTableInline]


class TimeIndexAdmin(admin.ModelAdmin):

    list_display = ['time_index_id', 'start_time', 'end_time']


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(TimeIndex, TimeIndexAdmin)
admin.site.register(TimeTable)
