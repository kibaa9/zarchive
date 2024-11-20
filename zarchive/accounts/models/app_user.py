from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from zarchive.accounts.managers import UserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=100,
        unique=True,
    )

    email = models.EmailField(
        max_length=100,
        unique=True,
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username

    objects = UserManager()
