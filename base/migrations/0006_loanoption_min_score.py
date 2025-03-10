# Generated by Django 5.1.4 on 2024-12-17 03:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_loanoption"),
    ]

    operations = [
        migrations.AddField(
            model_name="loanoption",
            name="min_score",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                max_digits=4,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(10.0),
                ],
            ),
            preserve_default=False,
        ),
    ]
