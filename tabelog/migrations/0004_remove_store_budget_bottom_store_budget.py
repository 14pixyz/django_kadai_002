# Generated by Django 4.2.11 on 2024-05-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelog', '0003_remove_store_budget_store_budget_bottom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='budget_bottom',
        ),
        migrations.AddField(
            model_name='store',
            name='budget',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
