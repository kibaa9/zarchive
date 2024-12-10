# Generated by Django 5.1.3 on 2024-12-09 21:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20241209_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]