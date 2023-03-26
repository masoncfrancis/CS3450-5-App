from django.http import HttpResponse
from django.shortcuts import render
from carRental.models import Vehicle, Reservation, Customer
from datetime import date
from decimal import *
import pprint
from django.contrib.auth.models import User

# Create your views here.


def car_page(request):
    typeOfCar = int(request.POST['type'])
    start = str(request.POST['start'])
    end = str(request.POST['end'])

    try:
        startDate = date.fromisoformat(start)
        endDate = date.fromisoformat(end)
    except ValueError:
        return HttpResponse("Error!")

    if (typeOfCar == 0):
        vehicles = Vehicle.objects.filter(price=50)
    elif (typeOfCar == 1):
        vehicles = Vehicle.objects.filter(price=75)
    elif (typeOfCar == 2):
        vehicles = Vehicle.objects.filter(price=100)
    else:
        vehicles = Vehicle.objects.all()

    cars = []
    for vehicle in vehicles:
        reservations = vehicle.reservation_set.filter(start__range=[startDate, endDate]).filter(end__range=[startDate,endDate])
        res = vehicle.reservation_set.filter(start__lte=start).filter(end__gte=end)
        if len(reservations) == 0 and len(res) == 0:
            cars.append(vehicle)
        else:
            continue
        
    context = {'cars': cars, start:start, end:end }
    return render(request, 'carRental/cars.html', context)


def account_page(request):
    #pprint.pprint(f"\n*** POST dictionary: {request.POST}\m")

    # Updating User Info
    new_first_name = str(request.POST.get('new_first_name', ""))
    new_last_name = str(request.POST.get('new_last_name', ""))
    new_email = str(request.POST.get('new_email', ""))

    user = User.objects.get(username=request.user.username)

    if new_first_name != "":
        user.first_name = new_first_name
        user.save()
    if new_last_name != "":
        user.last_name = new_last_name
        user.save()
    if new_email != "":
        user.email = new_email
        user.save()

    # Updating Customer Balance
    new_funds = Decimal(request.POST.get('funds', 0))
    customer_list = Customer.objects.filter(user__username=request.user)
    customer = customer_list[0]
    customer.addMoney(new_funds)

    context = {'balance': customer.balance}
    return render(request, 'carRental/account.html', context)