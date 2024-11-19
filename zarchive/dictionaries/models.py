from django.db import models

from zarchive.books.models import Book


class Dictionary(models.Model):
    book_words = models.CharField(
        max_length=120,
    )

    translated_word = models.CharField(
        max_length=120,
    )

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='dictionaries',
    )
