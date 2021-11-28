import datetime as datetime
from django.db import models
from django.db.models import TextChoices


class Route(models.Model):
    driver = models.ForeignKey('driver.Driver', models.PROTECT, verbose_name='Водитель')
    location_from = models.CharField('Место откуда', max_length=120)
    location_to = models.CharField('Место куда', max_length=120)
    passenger_price = models.PositiveIntegerField('Цена за пассажира', blank=True, null=True)
    cargo_price = models.PositiveIntegerField('Цена за кубический метр груза', blank=True, null=True)
    check_in_price = models.PositiveIntegerField('Цена заезда за 1 км от точки старта', blank=True, default=0)
    comment = models.TextField('Комментарий', blank=True, default='')
    start = models.DateTimeField('Дата старта', default=datetime.datetime.now)
    finish = models.DateTimeField('Дата прибытия', default=datetime.datetime.now)
    finished = models.BooleanField('Завершено', default=False)

    @property
    def total_price(self):
        return sum([x.amount for x in self.requests.all()])

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class RouteRequest(models.Model):
    class RouteRequestStatus(TextChoices):
        PAID = 'PAID'
        ACCEPTED = 'ACCEPTED'
        WAITING = 'WAITING'
        CANCELED = 'CANCELED'

    route = models.ForeignKey('Route', models.CASCADE, related_name='requests')
    user = models.ForeignKey('users.User', models.CASCADE, related_name='requests')
    passengers_count = models.PositiveIntegerField('Количество пассажиров')
    kids_count = models.PositiveIntegerField('Количество детей', blank=True, default=0)
    cargo_count = models.PositiveIntegerField('Количество единиц груза', blank=True, default=0)
    check_in_length = models.PositiveIntegerField('Расстояние до заезда в километрах', default=0)
    check_in_location = models.CharField('Место заезда', max_length=120, blank=True, default=None, null=True)
    status = models.CharField('Статус заявки', max_length=20, choices=RouteRequestStatus.choices,
                              default=RouteRequestStatus.WAITING)
    comment = models.TextField('Комментарий пассажира', default='', blank=True)
    comment_driver = models.TextField('Комментарий водителя', default='', blank=True)
    amount = models.PositiveIntegerField('Общая стоимость заказа', null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
