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

    def getAmountOwed(self):
        return self.hours * self.rate

    def __str__(self) -> str:
        return self.user.username

class Manager(Employee):

    def hire(self, newHire):
        n = Employee(customer_ptr=newHire)
        n.save()

    def payEmployees(self):
        employee_list = Employee.objects.all()
        for emp in employee_list:
            if (emp.user == self.user):
                self.hours = 0
                self.save()
                continue
            emp.addMoney(emp.hours * emp.rate)
            self.balance -= emp.hours * emp.rate
            emp.hours = 0
            self.hours = 0
            self.save()
            emp.save()

    def payEmployee(self, emp):
        emp.addMoney(emp.hours * emp.rate)
        self.balance -= emp.hours * emp.rate
        emp.hours = 0
        emp.save()
        self.save()

    def getAmountOwed(self):
        amount = 0
        for emp in Employee.objects.exclude(user=self.user):
            amount += emp.hours * emp.rate
        return amount


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
    disabled = models.BooleanField(default=False)
    photoFileName = models.CharField(max_length=35, default='')

    def __str__(self) -> str:
        return self.year + ", " + self.make + " " + self.model

    def getStatus(self) -> STATUS:
        return self.STATUS[self.status]


class Reservation(models.Model):
    STATUS = [
        ('AWAIT','Awaiting'),
        ('RENT', 'Rented'),
        ('DIS', 'Returned')
    ]
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    insurance = models.BooleanField(default=False)
    status = models.CharField(max_length = 10,choices = STATUS, default='AWAIT')
    confirmation_code = models.CharField(max_length=5, unique=True)
    def checkOut(self):
        self.status = 'RENT'
        self.save()

    
    def returnVehicle(self):
        self.vehicle.status = 'AV'
        self.vehicle.save()
        self.delete()

class Complaint(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

