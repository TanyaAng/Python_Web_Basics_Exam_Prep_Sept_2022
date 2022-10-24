from django.shortcuts import render

from GamesPlay.game.models import Game




def game_create(request):
    return render(request, 'game/create-game.html')


def game_details(request, pk):
    return render(request, 'game/details-game.html')


def game_edit(request, pk):
    return render(request, 'game/edit-game.html')


def game_delete(request, pk):
    return render(request, 'game/delete-game.html')
