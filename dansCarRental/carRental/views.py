from django.http import HttpResponse
from django.shortcuts import render, redirect
from carRental.models import Vehicle, Reservation, Customer, Complaint, Manager, Employee
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
    
    if endDate < startDate:
        return HttpResponse("Error! Invalid Dates")

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
        res = vehicle.reservation_set.filter(start__gte=start).filter(end__lte=end)
        if len(reservations) == 0 and len(res) == 0:
            cars.append(vehicle)
        else:
            continue
        
    context = {'cars': cars, start:start, end:end }
    return render(request, 'carRental/cars.html', context)


def checkout(request):
    pass


def account_page(request):
    #pprint.pprint(f"\n*** POST dictionary: {request.POST}\m")

    # Filing Complaint and Returning List of Complaints
    if request.POST.get('complaint') != '':
        complaint_text = str(request.POST.get('complaint'))
        complaint = Complaint(user=request.user, description=complaint_text)
        complaint.save()

    complaints = Complaint.objects.filter(user__username=request.user)

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
    new_funds_form = request.POST.get("funds", 0)

    if new_funds_form == "":
        new_funds_form = "0"

    new_funds = Decimal(new_funds_form)

    # new_funds = Decimal(request.POST.get('funds', 0))
    customer_list = Customer.objects.filter(user__username=request.user)
    customer = customer_list[0]
    customer.addMoney(new_funds)

    context = {'balance': customer.balance, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email, 'complaints': complaints}
    return render(request, 'carRental/account.html', context)


def home(request):
    context = {"employee": False}
    if request.user.is_authenticated:
        if Manager.objects.filter(user=request.user).exists() or Employee.objects.filter(user=request.user).exists() or request.user.is_superuser:
            context["employee"] = True
    return render(request, 'carRental/home.html', context)


def rented_cars(request):
    auth = False
    if request.user.is_authenticated:
        if Manager.objects.filter(user=request.user).exists() or Employee.objects.filter(user=request.user).exists() or request.user.is_superuser:
            auth = True

    if not auth:
        return HttpResponse("You are not authorized to view this page")
    
        
    context={"employee": True}
    overdue = Reservation.objects.filter(status="RENT").filter(end__lt=date.today()).filter(vehicle__disabled = False)
    rented = Reservation.objects.all().filter(status="RENT").filter(end__gte=date.today()).filter(vehicle__disabled = False)
    disabled = Vehicle.objects.all().filter(disabled=True)
    context["disabled"] = disabled
    context["overdue"] = overdue
    context["rented"] = rented
    return render(request, 'carRental/rentedCars.html', context)


def lojack(request):
    auth = False
    if request.user.is_authenticated:
        if Manager.objects.filter(user=request.user).exists() or Employee.objects.filter(user=request.user).exists() or request.user.is_superuser:
            auth = True

    if not auth:
        return HttpResponse("You are not authorized to view this page")
    

    if request.method == "POST" and auth:
        pk = request.POST['pk']
        vehicle = Vehicle.objects.get(id=pk)
        vehicle.disabled = not vehicle.disabled
        vehicle.save()
        return redirect('rentedCars')
    else :
        return HttpResponse("Error!")

