from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )
