from django.db import models


class AppUser(models.Model):
    username = models.CharField(
        max_length=100,
        unique=True,
    )

    email = models.EmailField(
        max_length=100,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
