from django.contrib.auth.models import User
from django.db import models

# # Create your models here.
# class UserProfile(models.Models):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # picture = models.TextField(null=True, blank=True)


class Cities(models.Model):
    city = models.CharField(max_length=15)
    code = models.CharField(max_length=4)


class Ride(models.Model):
    user_name = models.CharField(default="", max_length=50)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    journey_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    seat_available = models.IntegerField()


class OfferRide(Ride):
    origin_location = models.CharField(max_length=50)
    destination_location = models.CharField(max_length=50)
    contact = models.IntegerField()
    fare = models.IntegerField()