# Generated by Django 5.1.4 on 2024-12-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_alter_investmentoption_liquidity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="investmentoption",
            name="image",
            field=models.URLField(),
        ),
    ]