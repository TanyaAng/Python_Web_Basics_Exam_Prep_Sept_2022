from django.shortcuts import render

from GamesPlay.common.helpers import get_profile, get_all_games




def home_page(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'common/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    context = {
        'profile': profile,
        'games': get_all_games(),

    }
    return render(request, 'common/dashboard.html', context)
