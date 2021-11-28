from rest_framework import serializers

from route.models import Route, RouteRequest


class RouterBaseSerializer(serializers.ModelSerializer):
    free_places = serializers.SerializerMethodField(read_only=True)
    free_kids_places = serializers.SerializerMethodField(read_only=True)

    def get_free_places(self, obj: Route):
        places = obj.driver.car.places
        return places

    def get_free_kids_places(self, obj: Route):
        places = obj.driver.car.kids
        return places


class RouteListSerializer(RouterBaseSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class RouteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        exclude = ['driver', 'finished']


class RouteDetailSerializer(RouterBaseSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class RouteRequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteRequest
        fields = '__all__'


class RouteRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteRequest
        exclude = ['route', 'user', 'status', 'comment_driver', 'amount']
