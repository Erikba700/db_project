# Generated by Django 5.0.7 on 2024-08-31 02:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_owner",
            field=models.BooleanField(default=False),
        ),
    ]
