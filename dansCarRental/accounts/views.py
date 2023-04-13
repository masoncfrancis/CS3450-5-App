from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from carRental.models import Customer, Employee

class CustomerCreationForm(UserCreationForm):
    def save(self, commit=True):
        n_user = super(CustomerCreationForm, self).save(commit=True)
        n_customer = Customer()
        n_customer.user = n_user
        n_customer.save()
        return n_customer


class SignUpView(generic.CreateView):
    form_class = CustomerCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class EmployeeCreationForm(UserCreationForm):
    def save(self, commit=True):
        n_user = super(EmployeeCreationForm, self).save(commit=True)
        n_customer = Employee()
        n_customer.user = n_user
        n_customer.save()
        return n_customer

class SignUpViewEmployee(generic.CreateView):
    form_class = EmployeeCreationForm
    success_url = reverse_lazy("employees")
    template_name = "registration/signupEmployee.html"
    
