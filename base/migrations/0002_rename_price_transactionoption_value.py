# Generated by Django 5.1.4 on 2024-12-16 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transactionoption",
            old_name="price",
            new_name="value",
        ),
    ]