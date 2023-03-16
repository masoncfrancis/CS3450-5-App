from django.http import HttpResponse
from django.shortcuts import render
from carRental.models import Vehicle, Reservation
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
    flag = True
    for vehicle in vehicles:
        res = vehicle.reservation_set.filter(start__range=[startDate, endDate]).filter(end__range=[startDate,endDate])
        if res == None:
            cars.append(vehicle)
        else:
            continue
        
                
    
            
    context = {'cars': cars, start:start, end:end }
    return render(request, 'carRental/cars.html', context)
