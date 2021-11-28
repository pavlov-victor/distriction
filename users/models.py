from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField('Фамилия', max_length=120, default='')
    avatar = models.ImageField('Аватар', upload_to='users/avatars', blank=True, null=True)
    bonus = models.PositiveIntegerField('Количество бонусов', default=0)
