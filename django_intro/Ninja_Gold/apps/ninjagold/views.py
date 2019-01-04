from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'gold' not in request.session:
        request.session['gold']= 0
    gold = {
        'gold': request.session['gold'],
        'message': request.session['activity']}
    return render(request, "ninjagold/index.html", gold)

def process_money(request):
    if request.POST['building'] == "farm":
        farm = random.randint(10,20)
        request.session['gold'] += farm
        earned = 'Earned '+ str(farm) + ' golds from farm ' + '(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +')'
        request.session['activity'].append(earned)

    if request.POST['building'] == "cave":
        cave = random.randint(5,10)
        request.session['gold'] += cave
        earned = 'Earned '+ str(cave) + ' golds from cave ' + '(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +')'
        request.session['activity'].append(earned)

    if request.POST['building'] == "house":
        house = random.randint(2,5)
        request.session['gold'] += house
        earned = 'Earned '+ str(house) + ' golds from house ' + '(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +')'
        request.session['activity'].append(earned)

    if request.POST['building'] == "casino":
        casino = random.randint(-50,50)
        request.session['gold'] += casino
        if casino>=0:
            earned = 'Earned '+ str(casino) + ' golds from casino ' + '(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +')'
            request.session['activity'].append(earned)
        else:
            lost = 'Lost ' + str(-casino) + ' golds from casino...Ouch.' + '(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +')'
            request.session['activity'].append(lost)

    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")
