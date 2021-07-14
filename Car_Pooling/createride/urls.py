from django.urls import path
from . import views

app_name = "createride"
urlpatterns = [
    path('', views.createride, name="createride"),
]
