from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    url(r'^timetable/$', views.TimeTableView.as_view(), name='timetable'),
    url(r'^day/$', views.DateListView.as_view(), name='day'),
    url(r'^times/$', views.AvailableReservationTimeView.as_view(), name='times'),
    url(r'^reservation/$', views.MakeReservation.as_view(), name='reservation'),
]