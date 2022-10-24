from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GamesPlay.common.urls')),
    path('game/', include('GamesPlay.game.urls')),
    path('profile/', include('GamesPlay.app_profile.urls'))
]
