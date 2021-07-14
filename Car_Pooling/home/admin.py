from django.contrib import admin

from .models import Cities, Ride, OfferRide
# Register your models here.

admin.site.register(Cities)
admin.site.register(Ride)
admin.site.register(OfferRide)