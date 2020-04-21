from django.db import models
from room.models import Room
from datetime import datetime
from hotel.models import Hotel


# Create your models here.

class ReservationManager(models.Manager):
    pass


class Reservation(models.Model):
    reservation_id = models.IntegerField(primary_key=True)
    guest_id = models.IntegerField(default=1)  # should be fk user
    hotel_id = models.IntegerField(default=1)
    room_type = models.IntegerField(default=1)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservation')

    objects = ReservationManager()

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    @property
    def reservation_information(self):
        return f'Room by number: {self.reservation_id} booked by quest with id {self.guest_id}.'
