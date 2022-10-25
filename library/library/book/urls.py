from django.urls import path

from library.book.views import book_create, book_edit, book_details, book_delete

urlpatterns = (
    path('add/', book_create, name='book create'),
    path('edit/<int:pk>/', book_edit, name='book edit'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>/', book_delete, name='book delete'),
)