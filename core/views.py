from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def token_game(request):
    return render(request, 'token_game.html')