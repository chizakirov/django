from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.tv_app.models import *
from .models import Show
from datetime import datetime

def shows(request):
    context = {
        'all_shows' : Show.objects.all().values()
    }
    return render(request, "tv_app/shows.html",context)

def new(request):
    return render(request,"tv_app/new.html")

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'],release_date = request.POST['release_date'], description = request.POST['description'])
        id = new_show.id 
        messages.success(request, "Show successfully created")
        return redirect("/shows/" + str(id))

def display(request,id):
    new_show = Show.objects.get(id = id)
    context = {  
        'show': new_show
    }
    return render(request, "tv_app/newshow.html",context)

def show(request):
    id = request.POST['show']
    return redirect("/shows/" + str(id))

def edit(request, id):
        show = Show.objects.get(id = id)
        d = datetime.strftime(show.release_date, "%Y-%m-%d") #pay attention to date here
        print(d)
        context = {
            'show':show,
            'release_date': d
        }
        return render(request,"tv_app/editshow.html",context)

def update(request,id):
    errors = Show.objects.basic_validator(request.POST)
    # if Show.objects.filter("title" = postData['title']:
    #     errors["title2"] = "Show title already exists"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/" + str(id) + "/edit")
    else:
        show = Show.objects.get(id = id)
        show.title = str(request.POST['title'])
        show.network = str(request.POST['network'])
        show.release_date = str(request.POST['release_date'])
        show.description = str(request.POST['description'])
        show.save()
        messages.success(request, "Show successfully updated")
        return redirect("/shows/" + str(id))

def delete(request, id):
    show = Show.objects.get(id = id)
    show.delete()
    return redirect("/shows")