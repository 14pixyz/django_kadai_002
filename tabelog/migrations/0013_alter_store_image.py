# Generated by Django 4.2.11 on 2024-06-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelog', '0012_remove_favarit_update_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(default='noImage.png', null=True, upload_to=''),
        ),
    ]
