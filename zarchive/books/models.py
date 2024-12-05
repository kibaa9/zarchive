from django.core.validators import MinValueValidator, MaxValueValidator
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

    year_of_publish = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2100)]
    )

    publisher = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    cover_image = models.ImageField(
        upload_to='static/images/books/covers/',
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='books',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_available = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.title
