from rest_framework import serializers

from driver.models import Driver, Car, Report


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['driver']


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['driver']


class DriverCreateSerializer(serializers.ModelSerializer):
    car = CarCreateSerializer()

    class Meta:
        model = Driver
        exclude = ['user', 'is_active', 'is_verify']

    def save(self, **kwargs):
        car = kwargs.pop('car', None)
        obj = super(DriverCreateSerializer, self).save(**kwargs)
        serializer = CarCreateSerializer(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(driver=obj)
        return obj


class DriverDetailSerializer(serializers.ModelSerializer):
    car = CarDetailSerializer(read_only=True)

    class Meta:
        model = Driver
        fields = '__all__'


class DriverPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        exclude = ['user', 'is_active', 'is_verify']


class ReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude = ['user']
