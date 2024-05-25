# Generated by Django 4.2.11 on 2024-05-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelog', '0002_remove_store_category_store_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='budget',
        ),
        migrations.AddField(
            model_name='store',
            name='budget_bottom',
            field=models.PositiveIntegerField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]