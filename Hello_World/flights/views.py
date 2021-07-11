from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.


def index(req):
    return render(req, "flights/index.html", {"flights": Flight.objects.all()})


def flight(req, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(
        req, "flights/flight.html", {
            "flight": flight,
            "passengers": flight.passengers.all(),
            "non_passengers": Passenger.objects.exclude(flights=flight).all()
        })


def bookFlight(req, flight_id):
    if req.method == "POST":
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.get(
            pk=int(req.POST["passenger"])
        )  #we can use pk or id same thing as id is primary key but pk is more appropriate so from nxt pk
        passenger.flights.add(flight)
        return HttpResponseRedirect(
            reverse("flights:flight", args=(flight.id, )))
