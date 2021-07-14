from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Cities, OfferRide


# Create your views here.
def createride(request):
    if request.method == "POST":
        user_name = "dummy"
        origin = request.POST["origin"]
        destination = request.POST["destination"]
        journey_date = request.POST["journey_date"]
        seat_available = request.POST["seat_available"]
        origin_location = request.POST["origin_location"]
        destination_location = request.POST["destination_location"]
        contact = request.POST["contact"]
        fare = request.POST["fare"]
        # We will add validation later on
        OfferRide.objects.create(user_name=user_name,
                                 origin=origin,
                                 destination=destination,
                                 journey_date=journey_date,
                                 seat_available=seat_available,
                                 origin_location=origin_location,
                                 destination_location=destination_location,
                                 contact=contact,
                                 fare=fare)
        return HttpResponse("Successfully Added")

    cities = Cities.objects.all()
    return render(request, 'createride/createride.html', {"cities": cities})
