from django.urls import path

from notes_app.common.views import home_page

urlpatterns = (
    path('', home_page, name='home page'),
)
