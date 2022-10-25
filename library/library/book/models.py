from django.db import models


class Book(models.Model):
    TITLE_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
    )
