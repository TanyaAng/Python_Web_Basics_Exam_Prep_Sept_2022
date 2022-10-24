from django.urls import path

from Music_App.common.views import home_page

urlpatterns = (
    path('', home_page, name='home page'),
)