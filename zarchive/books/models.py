from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from zarchive.accounts.models import AppUser
from zarchive.authors.models import Author
from zarchive.books.validators import MinimalNumberValidator, MaximalNumberValidator
from zarchive.genres.models import Genre


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
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

    pages = models.PositiveSmallIntegerField(
        validators=(
            MinimalNumberValidator(0, "Pages should be more than 0"),
            MaximalNumberValidator(10000, "Pages should be less than 10000"))
    )

    year_of_publish = models.PositiveSmallIntegerField(
        validators=[
            MinimalNumberValidator(1800, "The year should be greater than 1800"),
            MaximalNumberValidator(2100, "The year should be less than 2100"),
        ]
    )

    publisher = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    cover_image = CloudinaryField(
        'image',
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

    is_approved = models.BooleanField(
        default=False,
    )

    class Meta:
        permissions = [
            ("can_approve_books", "Can approve books"),
        ]

    def __str__(self):
        return self.title
