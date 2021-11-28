import re

from rest_framework import serializers


def serializer_validate_phone_number(value):
    pattern = re.compile("^7[0-9]{10}")
    if not pattern.match(value):
        raise serializers.ValidationError('Номер телефона должен начинаться с 7 и иметь 11 символов')
