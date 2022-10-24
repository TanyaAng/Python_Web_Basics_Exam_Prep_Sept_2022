from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Game(models.Model):
    TITLE_MAX_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    LEVEL_MIN_VALUE = 1
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5

    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD = 'Board/Card Game'
    OTHER = 'Other'

    GAMES_LIST = [ACTION, ADVENTURE, PUZZLE, STRATEGY, SPORTS, BOARD, OTHER]
    CHOICES = [(game, game) for game in GAMES_LIST]

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        choices=CHOICES,
    )

    rating = models.FloatField(
        validators=(MinValueValidator(RATING_MIN_VALUE), MaxValueValidator(RATING_MAX_VALUE)),
    )

    max_level = models.IntegerField(
        validators=(MinValueValidator(LEVEL_MIN_VALUE),),
        null=True,
        blank=True
    )

    image_url = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )
