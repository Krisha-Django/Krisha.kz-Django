from django.db import models
from room.models import Room
from datetime import datetime
from hotel.models import Hotel
from auth_.models import MyUser


# Create your models here.

class ReservationManager(models.Manager):
    pass


class Reservation(models.Model):
    guest = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="reservations")
    description = models.CharField(max_length=300, default="Description")
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    terminate = models.BooleanField(default=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservation')

    objects = ReservationManager()

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    @property
    def reservation_information(self):
        return f'Room  {self.room} booked by quest with id {self.guest}.'

    def __str__(self):
        return self.description
