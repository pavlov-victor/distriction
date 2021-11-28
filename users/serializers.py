from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from driver.serializers import DriverDetailSerializer, CarDetailSerializer
from users.models import User
from utils.validators import serializer_validate_phone_number


class UserSelfSerializer(serializers.ModelSerializer):
    driver = serializers.SerializerMethodField(read_only=True)
    car = serializers.SerializerMethodField(read_only=True)

    @swagger_serializer_method(serializer_or_field=DriverDetailSerializer)
    def get_driver(self, obj: User):
        if hasattr(obj, 'driver'):
            return DriverDetailSerializer(obj.driver).data
        return None

    @swagger_serializer_method(serializer_or_field=CarDetailSerializer)
    def get_car(self, obj: User):
        if hasattr(obj, 'driver'):
            if hasattr(obj.driver, 'car'):
                return CarDetailSerializer(obj.driver.car).data
        return None

    class Meta:
        model = User
        fields = '__all__'


class UserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'patronymic', 'avatar', 'email']


class RegistrationSerializer(serializers.Serializer):
    phone = serializers.CharField(label='Номер телефона', validators=[serializer_validate_phone_number])

    def validate_phone(self, value):
        print(value)
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Данный номер телефона уже зарегистрирован')
        return value
