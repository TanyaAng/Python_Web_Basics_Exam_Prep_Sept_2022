from django import forms

from library.book.models import Book


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CreateBookForm(BaseBookForm):
    pass


class EditBookForm(BaseBookForm):
    pass


# class DeleteBookForm(BaseBookForm):
#     pass
