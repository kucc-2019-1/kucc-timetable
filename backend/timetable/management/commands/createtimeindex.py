from datetime import time, timedelta, datetime, date

from django.core.management import BaseCommand

from timetable.models import TimeIndex


class Command(BaseCommand):
    help = 'TimeIndex 초기화에 사용'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        time_order = 0
        current_time = time(9)
        end_time = time(23)
        delta = timedelta(minutes=30)

        while current_time < end_time:
            next_time = datetime.combine(date.today(), current_time) + delta
            TimeIndex(
                time_index_id=time_order,
                start_time=current_time,
                end_time=next_time.time()
            ).save()
            current_time = next_time.time()
            time_order += 1
