from django.urls import path

from . import views

app_name = "connect"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]