# Generated by Django 5.1.4 on 2024-12-17 02:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_remove_transaction_avaiable_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DepositOption",
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
                ("method", models.CharField(max_length=32)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("base.transactionoption",),
        ),
        migrations.CreateModel(
            name="TransferOption",
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
                (
                    "destiny",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destiny",
                        to=settings.AUTH_USER_MODEL,
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
