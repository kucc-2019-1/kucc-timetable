from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('reservation', views.ReservationViewSet)
router.register('time_index', views.Time_indexViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^timetable/$', views.TimeTableView.as_view(), name='timetable'),
    url(r'^day/$', views.DateListView.as_view(), name='day'),
]