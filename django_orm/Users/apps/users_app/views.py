from django.shortcuts import render

def index(request):
    return render(request, "users_app/index.html")