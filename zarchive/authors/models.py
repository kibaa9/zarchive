from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

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

    profile_picture = models.ImageField(
        upload_to='static/images/author_profile_pictures',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
