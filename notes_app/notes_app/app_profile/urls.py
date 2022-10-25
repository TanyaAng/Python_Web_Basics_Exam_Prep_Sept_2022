from django.urls import path

from notes_app.app_profile.views import profile_details, profile_delete

urlpatterns = (
    path('profile/', profile_details, name='profile details'),
    path('profile/delete', profile_delete, name='profile delete')
)
