from .models import Employee, Person
from .forms import EmployeeForm
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            department = form.cleaned_data["department"]
            gender = form.cleaned_data["gender"]

            person = Person.objects.create(first_name=first_name,
                                           last_name=last_name,
                                           gender=gender)
            employee = Employee.objects.create(profile=person,
                                               department=department)

            return HttpResponse("Added Successfully")
        else:
            return render(request, "modelBasics/index.html", {"form": form})

    return render(request, "modelBasics/index.html", {
        "form": EmployeeForm(),
        "lst": [1, 2, 3, 4, 5, 6]
    })
