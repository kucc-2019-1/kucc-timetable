# Generated by Django 2.1.4 on 2019-04-07 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
        migrations.CreateModel(
            name='TimeIndex',
            fields=[
                ('time_index_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'db_table': 'time_index',
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('time_table_id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.DateField()),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='timetable.Reservation')),
                ('time_index', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='timetable.TimeIndex')),
            ],
            options={
                'db_table': 'time_slot',
            },
        ),
    ]
