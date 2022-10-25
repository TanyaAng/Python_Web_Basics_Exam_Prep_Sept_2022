from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 30
    INGREDIENTS_MAX_LENGTH = 250
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LENGTH,
        null=False,
        blank=False,
    )

    time = models.IntegerField()
