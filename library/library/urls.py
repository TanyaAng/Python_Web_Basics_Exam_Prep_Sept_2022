from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.common.urls')),
    path('', include('library.book.urls')),
    path('profile/', include('library.app_profile.urls')),
]
