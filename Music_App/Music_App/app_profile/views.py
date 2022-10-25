from django.shortcuts import render, redirect

from Music_App.album.models import Album
from Music_App.app_profile.forms import DeleteProfileForm
from Music_App.common.helpers import get_profile, get_user_albums


def profile_details(request):
    context = {
        # 'profile': get_profile(),
        'albums': get_user_albums(),
    }
    return render(request, 'profile/profile-details.html', context)


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
    return render(request, 'profile/profile-delete.html', context)
