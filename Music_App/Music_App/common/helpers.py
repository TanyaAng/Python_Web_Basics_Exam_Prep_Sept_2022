from Music_App.album.models import Album
from Music_App.app_profile.models import Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return Profile.objects.all()[0]
    return None

def get_user_albums():
    albums = Album.objects.all()
    if albums:
        return albums
    return None