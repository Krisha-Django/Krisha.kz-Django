from django.db import models
from room.models import Room
from datetime import datetime
from hotel.models import Hotel
from auth_.models import MyUser
from datetime import datetime
import pytz
from .validators import validated__date
from django.core.exceptions import ValidationError

utc = pytz.UTC


# Create your models here.

class ReservationManager(models.Manager):
    def terminated(self):
        return super(ReservationManager, self).get_queryset().filter(terminate=True)

    def in_use(self):
        return super(ReservationManager, self).get_queryset().filter(terminate=False)


class Reservation(models.Model):
    guest = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="reservations")
    description = models.CharField(max_length=300, default="Description")
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    terminate = models.BooleanField(default=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservation')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel', blank=True, null=True)

    def clean(self):
        start_date = self.start_date
        end_date = self.end_date
        if start_date > end_date:
            raise ValidationError("lel")

    objects = ReservationManager()

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    @property
    def reservation_information(self):
        return f'Room  {self.room} booked by quest with id {self.guest}.'

    def __str__(self):
        return self.description
