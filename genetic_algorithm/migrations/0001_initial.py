# Generated by Django 4.2.1 on 2023-06-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genes', models.CharField(max_length=255)),
                ('fitness_score', models.FloatField(default=0.0)),
                ('generation', models.IntegerField(default=0)),
                ('has_albinism', models.BooleanField(default=False)),
            ],
        ),
    ]
