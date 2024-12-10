from cloudinary.models import CloudinaryField
from django.db import models
from django.utils.text import slugify
from zarchive.accounts.models import AppUser


class Profile(models.Model):
    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    date_of_registration = models.DateField(
        auto_now_add=True,
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
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
