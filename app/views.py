from django.shortcuts import render

from django.http import HttpResponse
from app.models import *

# Create your views here.
def form(request):
    if request.method == 'POST':
        
        gm = request.POST['gm']
        TO = game.objects.get_or_create(game_name = gm)
        return HttpResponse ('is inserted ')
    return render(request,'form.html')

def display_games(request):
    LOG = game.objects.all()
    d = {'LOG':LOG}
    return render(request,'display_games.html',d)
def insert_players(request):
    LOG = game.objects.all()
    d = {'LOG':LOG}
    if request.method == 'POST':
        gm = request.POST['gm']
        na = request.POST['na']
        em = request.POST['em']
        ag = request.POST['ag']
        co = request.POST['co']
        TO = game.objects.get(game_name = gm)
        PL = player_info.objects.get_or_create(game_name = TO,name = na,email = em,age = ag,country = co)
        return HttpResponse('inserted')
    return render(request,'insert_players.html',d)
def multiple_select(request):
     LOG = game.objects.all()
     d = {'LOG':LOG}
     if request.method == 'POST':
         MGL = request.POST.getlist('gm')
         EQST = player_info.objects.none()
         for to in MGL:
             EQST = EQST|player_info.objects.filter(game_name = to)
         d1 ={'EQST':EQST}
         return render(request,'display_players.html',d1)
    
     return render(request,'multiple_select.html',d)
def checkbox(request):
    LOG = game.objects.all()
    d = {"LOG":LOG}
    return render(request,'checkbox.html',d)

