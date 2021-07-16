from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from home.models import Cities, Ride, OfferRide
from django.forms import ValidationError

# Create your views here.


def getRide(request):
    if request.method == "POST":
        try:
            origin = request.POST["origin"]
            destination = request.POST["destination"]
            date = request.POST["date"]
            seats_required = request.POST["seat_available"]

            rides = Ride.objects.all().filter(
                origin=origin,
                destination=destination,
                seat_available__gte=seats_required,
                journey_date__gte=date)

            relatedRides = Ride.objects.all().filter(
                (Q(origin=origin)
                 | Q(destination=destination))
                & Q(journey_date__gte=date))

            return render(request, "getride/availability.html", {
                "rides": rides,
                "relatedRides": relatedRides
            })
        except ValidationError:
            return render(
                request, "home/index.html", {
                    'cities': Cities.objects.all(),
                    "validationerror": "Invalid queries"
                })

    return render(request, "getride/availability.html")


def chat(request, queryparams=None):
    if request.user.is_authenticated:
        print(request.user.username)
        return HttpResponse("hello world")
    else:
        print("Nope")
        return HttpResponse("goodbye:(")
