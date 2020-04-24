from datetime import datetime
import pytz

from django.core.exceptions import ValidationError

utc = pytz.UTC


def validated__date(value):
    if value < utc.localize(datetime.now()):
        raise ValidationError("Not correct date ")