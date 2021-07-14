from django.urls import path
from . import views

app_name = "getride"
urlpatterns = [
    path("<str:origintodestination>", views.getRide, name="getRide")
]
