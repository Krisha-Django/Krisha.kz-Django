from django.core.exceptions import ValidationError

MAX_FILE_SIZE = 100000000000
# Create your models here.
def validate_name(value):
    for char in value:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '-' or char == '&' or char == ' ':
            pass
        else:
            raise ValidationError("There is wrong symbols")


def validated_contact(value):
    if len(value) != 12 or value[0] != '+':
        raise ValidationError(" Write your number in format +77079864465")


def validated_image(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError('max file size is: {}'.format(MAX_FILE_SIZE))