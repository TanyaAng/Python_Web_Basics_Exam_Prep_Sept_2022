from django.shortcuts import render

from GamesPlay.common.helpers import get_profile, get_all_games

profile = get_profile()


def home_page(request):
    context = {
        'profile': profile,
    }
    return render(request, 'common/home-page.html', context)


def dashboard(request):
    context = {
        'profile': profile,
        'games': get_all_games(),

    }
    return render(request, 'common/dashboard.html', context)
