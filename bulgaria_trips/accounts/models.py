from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from bulgaria_trips.accounts.managers import BgTripUserManager


class BgTripUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
    )

    data_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'
    objects = BgTripUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
    )
    user = models.OneToOneField(
        BgTripUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from bulgaria_trips.accounts.signals import *
