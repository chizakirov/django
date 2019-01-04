from django.shortcuts import render, redirect
from django.contrib import messages
from apps.message.models import * 
from .models import Message

def wall(request):
    return render(request, "message/wall.html")
