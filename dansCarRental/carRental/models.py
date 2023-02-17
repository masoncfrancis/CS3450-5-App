from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        permissions=[
            ("mange_employees", "Can manage employees")
        ]
    
class Vehicle(models.Model):
    STATUS = [
        ('AV','Available'),
        ('RENT', 'Rented'),
        ('DIS', 'Disabled')
    ]
    TIER = [
        (100, 'High'),
        (75, "Middle"),
        (50, "Low")
    ]
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    price = models.IntegerField(choices=TIER)
    status = models.CharField(max_length=4, choices = STATUS, default='AV')

    def getStatus(self) -> STATUS:
        return self.STATUS[self.status]

class Reservation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    confirmation_code = models.CharField(max_length=5)
