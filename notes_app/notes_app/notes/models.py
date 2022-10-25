from django.db import models


class Note(models.Model):
    TITLE_MAX_LENGTH = 30
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )

    image_url = models.URLField()

    content = models.TextField()
