from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class NewTaskform(forms.Form):  # creates form without writing html form code
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label = "priority", min_value=1, max_value = 99)


def index(req):
    if "tasks" not in req.session:
        req.session["tasks"] = []
    return render(req, "tasks/index.html", {"tasks": req.session["tasks"]})


def add(req):
    if req.method == "POST":
        form = NewTaskform(
            req.POST)  # now all thst is Posted by user are in a var form
        if form.is_valid():
            task = form.cleaned_data["task"]
            req.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(req, "tasks/add.html", {"form": form})
    return render(req, "tasks/add.html", {"form": NewTaskform()})
