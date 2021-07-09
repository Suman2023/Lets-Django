from django.urls import path
from . import views

#There is a main urls.py for the whole project but we add for every app we create just for sake of simplicity and not cluttering the main urls.py
urlpatterns = [
    path("",views.index, name = "index"), #"" -> default route
    path("name", views.name, name = "name"), # this has url -> hello/name
    path("<str:name>",views.greet, name = "greet"), # here we pass any string after hello/<here> we return with Hello <here>
    
]
