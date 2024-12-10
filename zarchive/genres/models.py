from django.db import models

from zarchive.validators import AlphaValidator


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[AlphaValidator(), ],
    )

    def __str__(self):
        return self.name
