# Generated by Django 5.1.4 on 2024-12-17 03:26

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_depositoption_transferoption"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoanOption",
            fields=[
                (
                    "transactionoption_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.transactionoption",
                    ),
                ),
                ("installments", models.PositiveIntegerField()),
                (
                    "interest_ratio",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=4,
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(10.0),
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("base.transactionoption",),
        ),
    ]