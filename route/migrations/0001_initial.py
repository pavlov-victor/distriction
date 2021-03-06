# Generated by Django 3.2.9 on 2021-11-27 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_from', models.CharField(max_length=120, verbose_name='Место откуда')),
                ('location_to', models.CharField(max_length=120, verbose_name='Место куда')),
                ('passenger_price', models.PositiveIntegerField(verbose_name='Цена за пассаржира')),
                ('cargo_price', models.PositiveIntegerField(blank=True, default=0, verbose_name='Цена за кубический метр груза')),
                ('check_in_price', models.PositiveIntegerField(blank=True, default=0, verbose_name='Цена заезда за 1 км от точки старта')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Комментарий')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='driver.driver', verbose_name='Водитель')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
            },
        ),
        migrations.CreateModel(
            name='RouteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passengers_count', models.PositiveIntegerField(verbose_name='Количество пассажиров')),
                ('kids_count', models.PositiveIntegerField(blank=True, default=0, verbose_name='Количество детей')),
                ('cargo_count', models.PositiveIntegerField(blank=True, default=0, verbose_name='Количество единиц груза')),
                ('check_in_length', models.PositiveIntegerField(default=0, verbose_name='Расстояние до заезда в километрах')),
                ('status', models.CharField(choices=[('PAID', 'Paid'), ('ACCEPTED', 'Accepted'), ('WAITING', 'Waiting')], max_length=20, verbose_name='Статус заявки')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Комментарий пассажира')),
                ('comment_driver', models.TextField(blank=True, default='', verbose_name='Комментарий водителя')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='route.route')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказ',
            },
        ),
    ]
