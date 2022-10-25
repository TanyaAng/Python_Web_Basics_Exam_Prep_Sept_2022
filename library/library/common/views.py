from django.shortcuts import render, redirect

from library.app_profile.forms import CreateProfileForm
from library.app_profile.views import get_profile
from library.book.views import get_all_books


def home_page(request):
    profile = get_profile()
    if profile:
        books = get_all_books()
        context = {
            'profile': profile,
            'books': books,
            'show_nav_with_profile': True,
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
        'show_nav_with_profile': False,
    }
    return render(request, 'common/home-no-profile.html', context)
