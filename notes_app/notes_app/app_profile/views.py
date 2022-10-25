from django.shortcuts import render, redirect

from notes_app.app_profile.models import Profile
from notes_app.notes.models import Note


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def profile_details(request):
    notes = Note.objects.all()
    profile = get_profile()
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'profile/profile.html', context)


def profile_delete(request):
    profile = get_profile()
    Note.objects.all().delete()
    profile.delete()
    return redirect('home page')
