# Generated by Django 5.1.4 on 2024-12-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="investmentoption",
            name="quanitty",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
