from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('reservation', views.ReservationViewSet)
router.register('time_table', views.Time_tableViewSet)
router.register('time_index', views.Time_indexViewSet)

urlpatterns = [
    path('', include(router.urls))
]