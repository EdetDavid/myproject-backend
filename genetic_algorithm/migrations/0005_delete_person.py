# Generated by Django 4.2.5 on 2023-09-13 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("genetic_algorithm", "0004_person"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Person",
        ),
    ]
