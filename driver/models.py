from django.db import models
from django.db.models import TextChoices


class Driver(models.Model):
    class DriverStatus(TextChoices):
        OTHER = 'OTHER'
        IP = 'IP'
        LEGAL = 'LEGAL'

    user = models.OneToOneField('users.User', models.PROTECT)
    driving_experience = models.PositiveIntegerField('Стаж вождения', blank=True)
    driver_license = models.CharField('Водительское удостоверение', max_length=120, blank=True)
    carrier_license = models.CharField('Лицензия перевозчика', max_length=120, blank=True)
    status = models.CharField('Тип водителя', max_length=20,
                              choices=DriverStatus.choices, blank=True,
                              default=DriverStatus.OTHER)
    is_active = models.BooleanField('Активный', default=True)
    is_verify = models.BooleanField('Подтвержден', default=True)

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Car(models.Model):
    driver = models.OneToOneField('Driver', models.PROTECT, related_name='car')
    make = models.CharField('Марка машины', max_length=120, blank=True)
    number = models.CharField('Госномер', max_length=120, blank=True)
    places = models.PositiveIntegerField('Количество мест', blank=True)
    kids = models.PositiveIntegerField('Количество детских мест', default=0, blank=True)
    osago_number = models.CharField('Серия и номер', max_length=30, blank=True)
    osago_start = models.DateField('Дата регистрации', max_length=30, blank=True)
    osago_finish = models.DateField('Дата окончания', max_length=30, blank=True)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Report(models.Model):
    driver = models.ForeignKey('Driver', models.PROTECT, related_name='reports')
    text = models.TextField('Текст жалобы')
    user = models.ForeignKey('users.User', models.PROTECT, related_name='reports')

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'
