from django.shortcuts import render, redirect

from GamesPlay.app_profile.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from GamesPlay.common.helpers import get_profile, get_all_games




def profile_details(request):
    profile = get_profile()
    games = get_all_games()
    if games:
        count = games.count()
        average_rating = sum(game.rating for game in games) / games.count()
    else:
        count = 0
        average_rating = 0
    context = {
        'profile': profile,
        'games': games,
        'games_count': count,
        'average_rating': average_rating,
    }
    return render(request, 'profile/details-profile.html', context)


def profile_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'profile':profile,
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)
