from django.shortcuts import render, redirect

from notes_app.notes.forms import CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes_app.notes.models import Note


def get_all_notes():
    try:
        return Note.objects.all()
    except:
        return None

def note_details(request, id):
    note = Note.objects.filter(pk=id).get()
    context = {
        'note': note,
    }
    return render(request, 'notes/note-details.html', context)


def note_create(request):
    if request.method == 'GET':
        form = CreateNoteForm()
    else:
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
    }
    return render(request, 'notes/note-create.html', context)


def note_edit(request, id):
    note = Note.objects.filter(pk=id).get()
    if request.method == 'GET':
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'notes/note-edit.html', context)


def note_delete(request, id):
    note = Note.objects.filter(pk=id).get()
    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'notes/note-delete.html', context)
