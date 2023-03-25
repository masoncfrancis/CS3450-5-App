from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('cars', views.car_page, name="cars"),
    path('rentedCars', views.rented_cars, name="rentedCars"),
    path('loJack', views.loJack, name="loJack"),
    path('', views.home, name='home'),
    path('account', TemplateView.as_view(template_name='carRental/account.html'), name='account')
]