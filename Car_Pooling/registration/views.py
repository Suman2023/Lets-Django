from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LogInForm

# # # Create your views here.


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration:login')
        else:
            return render(request, "registration/signup.html", {'form': form})

    return render(request, "registration/signup.html", {'form': SignUpForm()})


def logout_view(request):
    logout(request)
    return render(request, 'home/index.html')


def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home:index')
            else:
                print(form)
                form.add_error(None, error='Inavlid Credentials')

                print(form)
                return render(request, 'registration/login.html',
                              {'form': form})

        else:
            return render(request, 'registration/login.html', {'form': form})
    return render(request, 'registration/login.html', {'form': LogInForm()})
