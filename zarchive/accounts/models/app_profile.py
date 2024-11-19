from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    date_of_registration = models.DateField(
        auto_now_add=True,
    )

    number_of_reviews = models.IntegerField(
        default=0,
    )
