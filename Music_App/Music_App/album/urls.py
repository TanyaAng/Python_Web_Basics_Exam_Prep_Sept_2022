from django.urls import path

from Music_App.album.views import album_create, album_details, album_edit, album_delete

urlpatterns =(
    path('add/', album_create, name='album create'),
    path('details/<int:pk>/', album_details, name='album details'),
    path('edit/<int:pk>/', album_edit, name='album edit'),
    path('delete/<int:pk>/', album_delete, name='album delete'),

)