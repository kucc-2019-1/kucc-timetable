from django.contrib import admin

from .models import Reservation, TimeIndex, TimeTable


class TimeIndexAdmin(admin.ModelAdmin):
    list_display = ['time_index_id', 'start_time', 'end_time']


admin.site.register(Reservation)
admin.site.register(TimeIndex, TimeIndexAdmin)
admin.site.register(TimeTable)
