from django.urls import path
from . import views

app_name = "getride"
urlpatterns = [
    path("", views.getRide, name="getRide"),
    path("chat/<str:queryparams>", views.chat, name="chat")
]
