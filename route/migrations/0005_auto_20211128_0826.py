# Generated by Django 3.2.9 on 2021-11-27 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_alter_routerequest_check_in_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='datetime',
        ),
        migrations.AddField(
            model_name='route',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата прибытия'),
        ),
        migrations.AddField(
            model_name='route',
            name='start',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата старта'),
        ),
        migrations.AlterField(
            model_name='routerequest',
            name='status',
            field=models.CharField(choices=[('PAID', 'Paid'), ('ACCEPTED', 'Accepted'), ('WAITING', 'Waiting'), ('CANCELED', 'Canceled')], default='WAITING', max_length=20, verbose_name='Статус заявки'),
        ),
    ]
