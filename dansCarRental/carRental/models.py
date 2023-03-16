from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)

    def addMoney(self, amount=0.00):
        self.balance += amount
        self.save()

    def __str__(self) -> str:
        return self.user.username


class Employee(Customer):
    hours = models.IntegerField(default=0)
    rate = models.DecimalField(default=15.00, max_digits=6, decimal_places=2)

    def addWorkedHours(self, hours=0):
        self.hours += hours
        self.save()

    def __str__(self) -> str:
        return self.user.username

class Manager(Employee):
    class Meta:
        permissions=[
            ("mange_employees", "Can manage employees")
        ]

    def hire(self, newHire):
        n = Employee()
        n.customer = newHire

    def payEmployees(self):
        employee_list = Employee.objects.all()
        for emp in employee_list:
            emp.addMoney(emp.hours * emp.rate)
            emp.hours = 0

    def __str__(self) -> str:
        return self.user.username
    
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

    def __str__(self) -> str:
        return self.year + ", " + self.make + " " + self.model

    def getStatus(self) -> STATUS:
        return self.STATUS[self.status]
    
    def pickUp():
        self.status = self.STATUS['RENT']
    
    def returnVehicle():
        self.status = self.STATUS['AV']

class Reservation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    confirmation_code = models.CharField(max_length=5)

class Complaint(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

