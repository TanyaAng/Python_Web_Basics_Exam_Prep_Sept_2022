from django.urls import path

from notes_app.notes.views import note_create, note_edit, note_delete, note_details

urlpatterns = (
    path('add/', note_create, name='note create'),
    path('edit/<int:id>/', note_edit, name='note edit'),
    path('delete/<int:id>/', note_delete, name='note delete'),
    path('details/<int:id>/', note_details, name='note details'),
)
