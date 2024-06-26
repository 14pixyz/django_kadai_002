# Generated by Django 4.2.11 on 2024-06-05 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabelog', '0010_alter_reservation_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favarit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tabelog.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
