from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account', views.account_page, name="account"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cars', views.car_page, name="cars"),
    path('', TemplateView.as_view(template_name='carRental/home.html'), name='home'),
    path('account', TemplateView.as_view(template_name='carRental/account.html'), name='account'),
    path('confirm_code', views.conf_ver_page, name="confirm_code"),
    path('loJack', views.lojack, name="lojack"),
    path('rentedCars', views.rented_cars, name="rentedCars"),
]