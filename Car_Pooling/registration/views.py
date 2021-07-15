# from django.core.exceptions import ValidationError
# from django.http.request import HttpRequest
# from django.http.response import HttpResponseRedirect
# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import login, logout, authenticate
# from django.http import HttpResponse

# # Create your views here.
# def signin(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]

#         user = authenticate()
#         if user:
#             login(user)
#             return render(request, "home/index.html")
#         else:
#             return HttpResponse("Error Credentials")

#     return render(request, "registration/signin.html")

# def register(request):
#     if request.method == "POST":
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         confirm_password = request.POST["confirm_password"]

#         #Do some validation

#         User.objects.create(username=username,
#                             password=password,
#                             email=email,
#                             first_name=first_name,
#                             last_name=last_name)

#         # return render(request, "registration/signin.html")
#         return HttpResponseRedirect('registraion:signin')

#     else:
#         return render(request, "registration/signup.html")

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def indexView(request):
    return render(request, 'registration/index.html')


@login_required()
def dashboardView(request):
    return render(request, 'registration/dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration:login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
