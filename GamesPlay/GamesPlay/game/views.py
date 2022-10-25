from django.shortcuts import render, redirect

from GamesPlay.common.helpers import get_profile
from GamesPlay.game.forms import CreateGameForm, EditGameForm, DeleteGameForm
from GamesPlay.game.models import Game




def game_details(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    context = {
        'game': game,
        'profile': profile,
    }
    return render(request, 'game/details-game.html', context)


def game_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'game/create-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }
    return render(request, 'game/edit-game.html', context)


def game_delete(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }
    return render(request, 'game/delete-game.html', context)
