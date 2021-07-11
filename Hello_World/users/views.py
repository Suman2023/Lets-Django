from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.


def index(req):
    if not req.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login_view"))
    else:
        return render(req, "users/user.html")


def login_view(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(req, "users/login.html",
                          {"message": "Invalid Credentials"})
    return render(req, "users/login.html")


def logout_view(req):
    logout(req)
    return render(req, "users/login.html",
                  {"message": "Logged Out Successfully"})
