from rest_framework import viewsets

from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserModel.objects.all()
    serializer_class = serializers.UserSerializer