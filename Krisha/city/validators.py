from django.core.exceptions import ValidationError


def validate_name(value):
    for char in value:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '-':
            pass
        else:
            raise ValidationError("There is wrong symbols")
