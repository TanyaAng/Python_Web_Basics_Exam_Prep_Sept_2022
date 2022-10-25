from django.shortcuts import render, redirect

from notes_app.app_profile.forms import CreateProfileForm
from notes_app.app_profile.views import get_profile
from notes_app.notes.views import get_all_notes


def home_page(request):
    profile = get_profile()

    if profile:
        notes = get_all_notes()
        context = {
            'profile': profile,
            'notes': notes,
        }
        return render(request, 'common/home-with-profile.html', context)
    if request.method == 'GET':
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
