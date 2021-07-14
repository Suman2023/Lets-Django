from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Cities, Ride, OfferRide
# Create your views here.


def index(request):
    cities = Cities.objects.all()
    return render(request, "home/index.html", {"cities": cities})
