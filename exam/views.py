from django.shortcuts import render
from .models import Developer, Game

def home(request):
    return render(request, 'exam/home.html')

def list_games(request):
    games = Game.objects.all()
    return render(request, 'exam/list_games.html', {'games':games})


