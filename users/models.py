from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def token(self):
        return RefreshToken.for_user(self)

    @property
    def full_name(self):
        return self.get_full_name()