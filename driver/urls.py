from django.urls import path

from driver.views import DriverAPIView, CarAPIView, ValidateLicenseAPIView, ReportAPIView

urlpatterns = [
    path('driver', DriverAPIView.as_view(), name='driver'),
    path('driver/report', ReportAPIView.as_view(), name='driver-report'),
    path('car', CarAPIView.as_view(), name='car'),
    path('validate_license', ValidateLicenseAPIView.as_view(), name='validate-license'),
]
