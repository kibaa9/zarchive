from cloudinary.models import CloudinaryField
from django.db import models
from django.utils.text import slugify

from zarchive.validators import AlphaValidator


class Author(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[AlphaValidator(), ],
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    date_of_death = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = CloudinaryField(
        'image',
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
