from django.shortcuts import render, redirect


from Music_App.album.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from Music_App.album.models import Album
from Music_App.common.helpers import get_profile


def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()
    profile = get_profile()
    context = {
        'album': album,
        'profile': profile,
    }

    return render(request, 'album/album-details.html', context)


def album_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'album/add-album.html', context)


def album_edit(request, pk):
    profile = get_profile()
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'album': album,
        'profile': profile,
    }
    return render(request, 'album/edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.filter(pk=pk).get()
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'album': album,
        'profile': profile,
    }
    print(form.errors)
    return render(request, 'album/delete-album.html', context)
