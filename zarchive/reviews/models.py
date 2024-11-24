from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from zarchive.accounts.models import AppUser
from zarchive.books.models import Book


class Review(models.Model):
    author = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    review = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
