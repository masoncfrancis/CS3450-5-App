from django.http import HttpResponse
from django.shortcuts import render, redirect
from carRental.models import Vehicle, Reservation, Manager, Employee
from datetime import date

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

def home(request):
    context = {"employee": False}
    if request.user.is_authenticated:
        if Manager.objects.filter(user=request.user).exists() or Employee.objects.filter(user=request.user).exists():
            context["employee"] = True
    return render(request, 'carRental/home.html', context)

def rented_cars(request):
    auth = False
    if request.user.is_authenticated:
        if Manager.objects.filter(user=request.user).exists() or Employee.objects.filter(user=request.user).exists():
            auth = True

    if not auth:
        return HttpResponse("You are not authorized to view this page")
    
        
    context={"employee": True}
    overdue = Reservation.objects.filter(status="RENT").filter(end__lt=date.today())
    rented = Reservation.objects.all().filter(status="RENT").filter(end__gte=date.today())
    disabled = Vehicle.objects.all().filter(disabled=True)
    context["disabled"] = disabled
    context["overdue"] = overdue
    context["rented"] = rented
    return render(request, 'carRental/rentedCars.html', context)


def lojack(request):
    auth = False
    if request.user.is_authenticated:
        if Manager.objects.filter(user=request.user).exists() or Employee.objects.filter(user=request.user).exists():
            auth = True

    if not auth:
        return HttpResponse("You are not authorized to view this page")
    

    if request.method == "POST" and auth:
        pk = request.POST['pk']
        vehicle = Vehicle.objects.get(id=pk)
        vehicle.disabled = True
        vehicle.save()
        return redirect('rentedCars')
    else :
        return HttpResponse("Error!")