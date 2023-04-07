from django.urls import path

from .views import SignUpView, SignUpViewEmployee

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signupEmployee/', SignUpViewEmployee.as_view(), name='signupEmp'),
]