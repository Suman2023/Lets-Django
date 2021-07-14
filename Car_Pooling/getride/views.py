from django.shortcuts import render
from home.models import Cities, Ride, OfferRide
# Create your views here.


def getRide(request, origintodestination):
    if request.method == "POST":
        origin = request.POST["origin"]
        destination = request.POST["destination"]
        date = request.POST["date"]
        seats_required = request.POST["seat_available"]

        rides = Ride.objects.all().filter(origin=origin,
                                          destination=destination,
                                          seat_available=seats_required,
                                          journey_date=date)
        print(rides)
        hell = Ride.objects.all()
        print(hell[0].origin)
        print(hell[0].destination)
        print(hell[0].journey_date)
        print(hell[0].seat_available)
        sameOriginRides = Ride.objects.filter(origin=origin).all()

        return render(request, "getride/availability.html", {
            "rides": rides,
            "sameOriginRides": sameOriginRides
        })
