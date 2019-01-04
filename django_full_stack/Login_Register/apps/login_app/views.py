from django.shortcuts import render, redirect
from apps.login_app.models import * 
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "login_app/index.html")

def register(request):
    error = User.objects.register_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = User.objects.filter(email = request.POST['email'])
        context = {
            'user': user[0]
        }
        return render(request, "login_app/success.html", context)
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = User.objects.filter(email = request.POST['login_email'])
        context = {
            'user':user[0]
        }
        return render(request, "login_app/success.html", context)

def clear(request):
    request.session.clear()
    return redirect("/")