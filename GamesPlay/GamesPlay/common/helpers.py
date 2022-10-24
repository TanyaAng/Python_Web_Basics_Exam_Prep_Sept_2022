from GamesPlay.app_profile.models import Profile
from GamesPlay.game.models import Game


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None

def get_all_games():
    games=Game.objects.all()
    if games:
        return games
    return None