from django.db import models
from zarchive.authors.models import Author
from zarchive.genres.models import Genre
from zarchive.publishers.models import Publisher
from zarchive.series.models import Series


class Book(models.Model):
    title = models.CharField(
        max_length=100,
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='books',
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    pages = models.PositiveIntegerField()

    year_of_publish = models.PositiveSmallIntegerField()

    genre = models.ManyToManyField(
        to=Genre,
        related_name='books',
    )

    series = models.ForeignKey(
        to=Series,
        on_delete=models.SET_NULL,
        related_name='books',
        null=True,
    )

    publisher = models.ForeignKey(
        to=Publisher,
        on_delete=models.SET_NULL,
        related_name='books',
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    has_been_adapted = models.BooleanField(
        default=False,
    )

