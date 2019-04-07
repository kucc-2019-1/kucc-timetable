from django.contrib import admin

from .models import Reservation, TimeIndex, TimeTable


admin.site.register(Reservation)
admin.site.register(TimeIndex)
admin.site.register(TimeTable)
