from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from home.models import Cities, Ride, OfferRide

# Create your views here.


def getRide(request):
    if request.method == "POST":
        origin = request.POST["origin"]
        destination = request.POST["destination"]
        date = request.POST["date"]
        seats_required = request.POST["seat_available"]

        rides = Ride.objects.all().filter(origin=origin,
                                          destination=destination,
                                          seat_available__gte=seats_required,
                                          journey_date__gte=date)
        # print(rides)
        # hell = Ride.objects.all()
        # print(hell[0].origin)
        # print(hell[0].destination)
        # print(hell[0].journey_date)
        # print(hell[0].seat_available)

        relatedRides = Ride.objects.all().filter(
            Q(origin=origin) | Q(destination=destination))

        return render(request, "getride/availability.html", {
            "rides": rides,
            "relatedRides": relatedRides
        })
    return render(request, "getride/availability.html")


def chat(request, queryparams=None):
    if request.user.is_authenticated:
        print(request.user.username)
        return HttpResponse("hello world")
    else:
        print("Nope")
        return HttpResponse("goodbye:(")
