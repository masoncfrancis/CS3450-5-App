from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account', views.account_page, name="account"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cars', views.car_page, name="cars"),
    path('checkout', TemplateView.as_view(template_name='carRental/checkout.html'), name='checkout'),
    path('loJack', views.lojack, name="lojack"),
]