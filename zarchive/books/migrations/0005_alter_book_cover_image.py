# Generated by Django 5.1.3 on 2024-12-10 17:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
