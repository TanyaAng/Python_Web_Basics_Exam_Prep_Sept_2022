from django.core.exceptions import ValidationError


def only_letters_validator(input):
    for ch in input:
        if not ch.isalpha() and not ch.isdigit() and not ch == '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def positive_float_number(value):
    if value < 0:
        raise ValidationError('The price cannot be negative number.')
