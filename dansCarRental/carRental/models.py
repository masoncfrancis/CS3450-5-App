from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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

class Reservation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    start = models.DateField()
    end = models.DateField()
    confirmation_code = models.CharField(max_length=5)

class Complaint(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

