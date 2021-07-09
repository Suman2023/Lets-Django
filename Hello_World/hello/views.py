from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req): #req -> request
    return render(req, "hello\index.html")

def name(req):
    return HttpResponse("Hello, SUM4N!")

def greet(req, name):
    return render(req,"hello\greet.html",
    {
        "name": name.capitalize(),
    }) # passing some parameters to the link as name in dict