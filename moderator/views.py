from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from driver.models import Driver, Report
from route.models import Route
from users.models import User


def driver_change_status(request, pk):
    driver = Driver.objects.get(pk=pk)
    driver.is_active = not driver.is_active
    driver.save()
    return redirect('drivers-detail', pk=pk)


class IndexPageView(TemplateView):
    template_name = 'moderator/index.html'


class DriverDetailView(DetailView):
    template_name = 'moderator/driver_detail.html'
    queryset = Driver.objects.all()


class DriversPageView(ListView):
    template_name = 'moderator/drivers.html'
    queryset = Driver.objects.all().select_related('user')


class PassengersPageView(ListView):
    template_name = 'moderator/passengers.html'
    queryset = User.objects.all()


class RoutesPageView(ListView):
    template_name = 'moderator/routes.html'
    queryset = Route.objects.all()


class ReportsPageView(ListView):
    template_name = 'moderator/reports.html'
    queryset = Report.objects.all()
