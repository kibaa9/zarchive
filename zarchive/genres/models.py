from django.db import models

from zarchive.validators import LetterAndCommaValidator


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[LetterAndCommaValidator(), ],
    )

    def __str__(self):
        return self.name
