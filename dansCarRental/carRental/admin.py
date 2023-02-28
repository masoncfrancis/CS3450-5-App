from django.contrib import admin
from .models import Vehicle, Manager, Employee, Reservation, Customer

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Reservation)
admin.site.register(Customer)
