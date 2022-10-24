
from django.shortcuts import render, redirect

from Music_App.app_profile.forms import CreateProfileForm
from Music_App.app_profile.views import get_profile
from Music_App.common.helpers import get_user_albums


def home_page(request):
    profile = get_profile()
    if profile:
        albums = get_user_albums()
        context = {
            'albums': albums,
            'profile': profile,
        }
        return render(request, 'common/home-with-profile.html', context)
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
    }
    return render(request, 'common/home-no-profile.html', context)
