from django.shortcuts import render
from apps.ninjas_app.models import *

def index(request):
    context = {"dojos": Dojo.objects.all()}
    return render(request, "ninjas_app/index.html", context)
