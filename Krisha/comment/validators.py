from datetime import datetime
import pytz

from django.core.exceptions import ValidationError

utc = pytz.UTC

def validated_text(value):
    if len(value) <= 0:
        raise ValidationError("Please, Write comment")


def validated_created_date(value):
    print(value)
    if value < utc.localize(datetime.now()):
        raise ValidationError("Comment is created today")
