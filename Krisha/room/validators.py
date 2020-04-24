from django.core.exceptions import ValidationError


# Create your models here.


def validated_price(value):
    if value <= 0:
        raise ValidationError("Price can not be negative or zero")


def validated_room_number(value):
    if int(value)<=0:
        raise ValidationError("Number of room can not be zero on negative")
