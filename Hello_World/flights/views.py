from django.shortcuts import render
from .models import *
# Create your views here.


def index(req):
    return render(req, "flights/index.html", {"flights": Flight.objects.all()})


def flight(req, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(req, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })
