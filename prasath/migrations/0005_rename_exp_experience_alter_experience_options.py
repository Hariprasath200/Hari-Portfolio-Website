# Generated by Django 5.0.1 on 2024-01-07 16:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prasath", "0004_exp"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="exp",
            new_name="Experience",
        ),
        migrations.AlterModelOptions(
            name="experience",
            options={"verbose_name": "Experience", "verbose_name_plural": "Experience"},
        ),
    ]