from django.urls import path

from route.views import RouteAPIView, RouteDetailAPIView,\
    RequestAPIView, RequestAcceptAPIView, RequestCancelAPIView, \
    RouteFinishAPIView, RequestsAPIView

urlpatterns = [
    path('route', RouteAPIView.as_view(), name='route'),
    path('route/<pk>', RouteDetailAPIView.as_view(), name='route-detail'),
    path('route/<pk>/finish', RouteFinishAPIView.as_view(), name='route-finish'),
    path('route/<pk>/requests', RequestsAPIView.as_view(), name='route-list'),
    path('route/<pk>/request', RequestAPIView.as_view(), name='route-detail'),
    path('route/<route_pk>/request/<pk>/accept', RequestAcceptAPIView.as_view(), name='route-accept'),
    path('route/<route_pk>/request/<pk>/cancel', RequestCancelAPIView.as_view(), name='route-cancel'),
    path('route/<route_pk>/request/<pk>/payment', RequestCancelAPIView.as_view(), name='route-cancel'),
]
