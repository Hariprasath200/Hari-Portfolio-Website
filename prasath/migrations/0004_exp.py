# Generated by Django 5.0.1 on 2024-01-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prasath", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="exp",
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
                ("name", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="picture/")),
            ],
            options={
                "verbose_name": "exp",
                "verbose_name_plural": "exp",
            },
        ),
    ]
