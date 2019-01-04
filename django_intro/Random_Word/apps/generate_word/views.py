from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string 
import random
import string

def index(request):
    request.session['counter'] = 0 
    return render(request, "generate_word/index.html")

def random_word(request):
    random_word = ''.join([random.choice(string.ascii_letters) for n in range(14)])
    request.session['counter'] +=1 
    result = {
        'word': random_word,
        'counter': request.session['counter']
    }
    return render(request, "generate_word/index.html", result)

def reset(request):
    request.session.clear()
    return redirect("/")