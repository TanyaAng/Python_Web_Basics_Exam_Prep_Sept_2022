from django.shortcuts import render, redirect

from library.app_profile.forms import EditProfileForm, DeleteProfileForm
from library.app_profile.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile,
        'show_nav_with_profile': True,
    }
    return render(request, 'profile/details-profile.html', context)


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
        'form': form,
        'show_nav_with_profile': True,

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
        'show_nav_with_profile': True,

    }
    return render(request, 'profile/delete-profile.html', context)
