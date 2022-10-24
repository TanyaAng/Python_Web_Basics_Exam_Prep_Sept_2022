from django.core.validators import MinValueValidator
from django.db import models



class Profile(models.Model):
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    AGE_MIN_VALUE = 12

    email = models.EmailField()

    age = models.PositiveIntegerField(
        validators=(MinValueValidator(AGE_MIN_VALUE),)
    )

    password = models.CharField(max_length=PASSWORD_MAX_LENGTH, )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return None
