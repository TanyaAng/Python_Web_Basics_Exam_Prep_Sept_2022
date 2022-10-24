from django.shortcuts import render, redirect

from Music_App.album.models import Album
from Music_App.common.helpers import get_profile, get_user_albums


def profile_details(request):
    context = {
        'profile': get_profile(),
        'albums': get_user_albums(),
    }
    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Album.objects.all().delete()
        return redirect('home page')
    return render(request, 'profile/profile-delete.html')
