from django.db import models


class Publisher(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
