from datetime import datetime

import pytz
from django.core.exceptions import ValidationError
utc = pytz.UTC


def validate_birthday(value):
    if value > utc.localize(datetime.now()):
        raise ValidationError("Birthday date mistake")
