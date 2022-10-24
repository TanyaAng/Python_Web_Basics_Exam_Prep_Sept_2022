from django.db import models

from Music_App.common.validators import positive_float_number


class Album(models.Model):
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    R_and_B_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    MUSIC_GENGERS = [POP_MUSIC, JAZZ_MUSIC, R_and_B_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER]

    GENGERS = [(genre, genre) for genre in MUSIC_GENGERS]

    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    album_name = models.CharField(max_length=ALBUM_NAME_MAX_LENGTH,
                                  unique=True,
                                  )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENGERS,
    )

    description=models.TextField(
        null=True,
        blank=True,
    )

    image=models.URLField()

    price=models.FloatField(
        validators=(positive_float_number,)
    )
