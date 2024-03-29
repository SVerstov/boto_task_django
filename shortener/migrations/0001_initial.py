# Generated by Django 5.0.1 on 2024-01-28 08:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link_id", models.CharField(max_length=10, unique=True)),
                ("url", models.URLField()),
                ("created_by_ip", models.GenericIPAddressField(null=True)),
                ("counter", models.PositiveIntegerField(default=0)),
                (
                    "status_code",
                    models.PositiveIntegerField(
                        default=301,
                        validators=[
                            django.core.validators.MinValueValidator(300),
                            django.core.validators.MaxValueValidator(308),
                        ],
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
