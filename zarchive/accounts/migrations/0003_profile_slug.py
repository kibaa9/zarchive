# Generated by Django 5.1.3 on 2024-11-24 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_number_of_reviews_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
