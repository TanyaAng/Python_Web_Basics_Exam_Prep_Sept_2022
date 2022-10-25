from django.shortcuts import render, redirect

from library.book.forms import CreateBookForm, EditBookForm
from library.book.models import Book


def get_all_books():
    try:
        return Book.objects.all()
    except:
        return None


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()
    context = {
        'book': book,
        'show_nav_with_profile': True,
    }
    return render(request, 'book/book-details.html', context)


def book_create(request):
    if request.method == 'GET':
        form = CreateBookForm()
    else:
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'show_nav_with_profile': True,

    }
    return render(request, 'book/add-book.html', context)


def book_edit(request, pk):
    book = Book.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'book':book,
        'show_nav_with_profile': True,

    }
    return render(request, 'book/edit-book.html', context)


def book_delete(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('home page')
