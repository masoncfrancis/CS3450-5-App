from django.http import HttpResponse
from django.shortcuts import render
from carRental.models import Vehicle, Reservation
from datetime import date

# Create your views here.
def conf_ver_page(request):
    c_code = None
    try:
        checkingout = int(request.POST['checkout'])
    except:
        checkingout = 0
    try:
        c_code = int(request.POST['c_code'])
        reservation = Reservation.objects.get(confirmation_code=c_code)
        v_type = reservation.vehicle
    except:
        reservation = None
        v_type = None
    if checkingout == 1:
        if reservation != None:
            reservation.checkOut()
            checkingout = 2
        else:
            checkingout = 3
    context = {'c_code': c_code, 'reservation': reservation, 'v_type': v_type, 'checkingout' : checkingout}
    return render(request, 'carRental/conf_ver.html', context)


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
