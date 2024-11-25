from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    address = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
