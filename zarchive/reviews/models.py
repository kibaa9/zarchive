from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from zarchive.accounts.models import AppUser
from zarchive.books.models import Book


class Review(models.Model):
    class Meta:
        unique_together = ('book', 'user')

    user = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Review by {self.user.username} for {self.book.title}'
