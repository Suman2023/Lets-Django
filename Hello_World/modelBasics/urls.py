from django.urls import path
from . import views

app_name = "modelBasics"

urlpatterns = [
    path("", views.index, name="index"),
]
