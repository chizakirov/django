#---first_app---
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.timezone import utc
import datetime

def index(request):
    # return HttpResponse("views worked")
    context = {"time": strftime("%Y-%m-%d %H:%M %p", gmtime())}
    # context = {"time": datetime.datetime.utcnow().replace(tzinfo=utc)} # method 2
    return render(request,"time_display/index.html", context)