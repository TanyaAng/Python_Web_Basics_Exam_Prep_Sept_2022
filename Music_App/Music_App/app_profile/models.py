from django.core.validators import MinLengthValidator
from django.db import models

from Music_App.common.validators import only_letters_validator


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    username = models.CharField(max_length=USERNAME_MAX_LENGTH,
                                validators=(MinLengthValidator(USERNAME_MIN_LENGTH), only_letters_validator),
                                )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
