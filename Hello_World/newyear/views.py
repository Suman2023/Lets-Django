import datetime
from django.shortcuts import render

# Create your views here.

def index(req):
    now = datetime.datetime.now()
    return render(req, "newyear\index.html",{
        "newyear": now.month == 1 and now.day == 1
    })
