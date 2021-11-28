from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegistrationAPIView, UserAPIView

urlpatterns = [
    path('registration', RegistrationAPIView.as_view(), name='user-registration'),
    path('login', obtain_auth_token, name='login'),
    path('user', UserAPIView.as_view(), name='user'),
]
