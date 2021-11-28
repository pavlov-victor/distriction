import requests
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd

from driver.serializers import DriverDetailSerializer, DriverCreateSerializer, DriverPatchSerializer, \
    CarPatchSerializer, CarCreateSerializer, CarDetailSerializer, ReportCreateSerializer
from utils.serializers import SuccessSerializer


class DriverAPIView(APIView):

    @swagger_auto_schema(responses={200: DriverDetailSerializer()})
    def get(self, request, *args, **kwargs):
        serializer = DriverDetailSerializer(self.request.user.driver)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DriverCreateSerializer(), responses={201: SuccessSerializer()})
    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'driver'):
            return Response({'driver': 'У вас уже есть профиль водителя'}, 400)
        serializer = DriverCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({'success': True})

    @swagger_auto_schema(request_body=DriverPatchSerializer(), responses={200: SuccessSerializer()})
    def patch(self, request, *args, **kwargs):
        serializer = DriverPatchSerializer(request.user.driver, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True})


class CarAPIView(APIView):
    @swagger_auto_schema(responses={200: CarDetailSerializer()})
    def get(self, request, *args, **kwargs):
        serializer = CarDetailSerializer(request.user.driver.car)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CarCreateSerializer(), responses={200: SuccessSerializer()})
    def post(self, request, *args, **kwargs):
        if hasattr(request.user.driver, 'car'):
            return Response({'driver': 'У вас уже есть машина'}, 400)
        serializer = CarCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(driver=request.user.driver)
        return Response({'success': True})

    @swagger_auto_schema(request_body=CarPatchSerializer(), responses={200: SuccessSerializer()})
    def patch(self, request, *args, **kwargs):
        serializer = CarPatchSerializer(request.user.driver.car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True})


class ValidateLicenseAPIView(APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('license', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    def get(self, request, *args, **kwargs):
        print(request.query_params.get('license'))
        tables = pd.read_html(
            f'https://mintrans.sakha.gov.ru/utable/front/report/?UtableReport%5Bnum_reestr%5D={request.GET.get("license", None)}&UtableReport%5Bdate_send%5D=&UtableReport%5Bportal%5D=&UtableReport%5Bgos_reg_znak%5D=&UtableReport%5Btitle%5D=&UtableReport%5Bdate_reestr%5D=&UtableReport%5Bnum_utable%5D=&UtableReport%5Bseriya%5D=&UtableReport%5Bmarka_ts%5D=&UtableReport%5Bmodel_ts%5D=&UtableReport%5Bdate_priostanova%5D=&UtableReport%5Bsrok_priostanova%5D=&UtableReport%5Bdate_annulir%5D=&UtableReport%5Bprichina_annul%5D=&UtableReport%5Bosobie_metki%5D=&UtableReport_page=1'
        )
        table = tables[0]
        if table.shape[0] < 3:
            return Response({'status': False, 'data': {}})
        table = table.fillna('')
        return Response({'status': True, 'data': table.to_dict('records')[1]})


class ReportAPIView(APIView):
    @swagger_auto_schema(request_body=ReportCreateSerializer(), responses={201: SuccessSerializer()})
    def post(self, request, *args, **kwargs):
        serializer = ReportCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({'success': True}, 201)
