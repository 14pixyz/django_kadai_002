# Generated by Django 4.2.11 on 2024-06-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelog', '0009_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(),
        ),
    ]
