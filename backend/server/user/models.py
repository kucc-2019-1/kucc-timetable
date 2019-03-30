from django.db import models


class UserModel(models.Model):
    user_ID = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)