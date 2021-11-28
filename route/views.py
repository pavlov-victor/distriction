from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from route.models import Route, RouteRequest
from route.serializers import RouteListSerializer, RouteCreateSerializer, RouteDetailSerializer, \
    RouteRequestDetailSerializer, RouteRequestCreateSerializer
from utils.serializers import SuccessSerializer


class RouteAPIView(APIView):

    @swagger_auto_schema(responses={200: RouteListSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        queryset = Route.objects.all()
        serializer = RouteListSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RouteCreateSerializer(), responses={201: SuccessSerializer()})
    def post(self, request, *args, **kwargs):
        serializers = RouteCreateSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save(driver=request.user.driver)
        return Response({'success': True})


class RouteDetailAPIView(APIView):

    @swagger_auto_schema(responses={200: RouteDetailSerializer()})
    def get(self, request, *args, **kwargs):
        route = Route.objects.get(id=kwargs['pk'])
        return Response(RouteDetailSerializer(route).data)

    @swagger_auto_schema(responses={204: SuccessSerializer()})
    def delete(self, request, *args, **kwargs):
        route = Route.objects.get(id=kwargs['pk'])
        route.delete()
        return Response({'success': True}, 204)


class RouteFinishAPIView(APIView):
    @swagger_auto_schema(responses={200: SuccessSerializer()})
    def get(self, request, *args, **kwargs):
        route = Route.objects.get(id=kwargs['pk'])
        route.finished = True
        route.save()
        return Response({'success': True})


class RequestsAPIView(APIView):

    @swagger_auto_schema(responses={200: RouteRequestDetailSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        route_requests = RouteRequest.objects.filter(route_id=kwargs['pk'])
        serializer = RouteRequestDetailSerializer(route_requests, many=True)
        return Response(serializer.data)


class RequestAPIView(APIView):

    @swagger_auto_schema(responses={200: RouteRequestDetailSerializer()})
    def get(self, request, *args, **kwargs):
        route_request = RouteRequest.objects.get(user=request.user)
        serializer = RouteRequestDetailSerializer(route_request)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RouteRequestCreateSerializer(), responses={201: SuccessSerializer()})
    def post(self, request, *args, **kwargs):
        route = Route.objects.get(id=kwargs['pk'])
        serializer = RouteRequestCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = self._count_amount(route, **serializer.validated_data)
        serializer.save(route=route, user=request.user, amount=amount)
        return Response({'success': True}, 201)

    @swagger_auto_schema(responses={204: SuccessSerializer()})
    def delete(self, request, *args, **kwargs):
        route_request = RouteRequest.objects.get(user=request.user, route_id=kwargs['pk'])
        route_request.delete()
        return Response({'success': True}, 204)

    def _count_amount(self, route: Route, **kwargs) -> int:
        amount = 0
        price_per_passenger = route.passenger_price
        price_per_cargo = route.cargo_price
        price_per_kilometer = route.check_in_price
        amount += (price_per_passenger * kwargs['passengers_count'])
        if price_per_cargo and 'cargo_count' in kwargs:
            amount += (price_per_cargo * kwargs['cargo_count'])
        if price_per_kilometer and 'check_in_length' in kwargs:
            amount += (price_per_kilometer * kwargs['length'])
        return amount


class RequestAcceptAPIView(APIView):

    @swagger_auto_schema(responses={200: SuccessSerializer()})
    def get(self, request, *args, **kwargs):
        route_request = RouteRequest.objects.get(user=request.user, route_id=kwargs['pk'])
        route_request.status = RouteRequest.RouteRequestStatus.ACCEPTED
        route_request.save()
        return Response({'success': True})


class RequestCancelAPIView(APIView):

    @swagger_auto_schema(responses={200: SuccessSerializer()})
    def get(self, request, *args, **kwargs):
        route_request = RouteRequest.objects.get(user=request.user, route_id=kwargs['pk'])
        route_request.status = RouteRequest.RouteRequestStatus.CANCELED
        route_request.save()
        return Response({'success': True})


class RequestPaymentAPIView(APIView):

    @swagger_auto_schema(responses={200: SuccessSerializer()})
    def get(self, request, *args, **kwargs):
        route_request = RouteRequest.objects.get(user=request.user)
        route_request.status = RouteRequest.RouteRequestStatus.PAID
        route_request.save()
        return Response({'success': True})
