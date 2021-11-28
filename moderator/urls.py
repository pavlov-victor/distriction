from django.urls import path

from moderator.views import IndexPageView, PassengersPageView, RoutesPageView, DriversPageView, ReportsPageView, \
    DriverDetailView, driver_change_status

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('pages/routes', RoutesPageView.as_view(), name='routes'),
    path('pages/reports', ReportsPageView.as_view(), name='reports'),
    path('pages/passengers', PassengersPageView.as_view(), name='passengers'),
    path('pages/drivers', DriversPageView.as_view(), name='drivers'),
    path('pages/drivers/<pk>', DriverDetailView.as_view(), name='drivers-detail'),
    path('pages/drivers/<pk>/change_status', driver_change_status, name='drivers-change_status'),
]
