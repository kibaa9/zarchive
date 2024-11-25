from django.db import models
from zarchive.accounts.models import AppUser
from zarchive.authors.models import Author
from zarchive.genres.models import Genre


class Book(models.Model):
    title = models.CharField(
        max_length=100,
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='books',
    )

    description = models.TextField()

    genre = models.ManyToManyField(
        to=Genre,
    )

    pages = models.PositiveSmallIntegerField()

    year_of_publish = models.PositiveSmallIntegerField()  # add validators

    publisher = models.CharField(
        max_length=100,
    )

    cover_image = models.ImageField(
        upload_to='static/images/books/covers/',
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        to=AppUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books',
    )

    def __str__(self):
        return self.title