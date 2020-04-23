from django.db import models
from hotel.models import Hotel
from auth_.models import MyUser


class RoomManager(models.Manager):
    pass


class RoomTypeManager(models.Manager):
    def single_rooms(self):
        return super(RoomTypeManager, self).get_queryset().filter(type=1)

    def double_rooms(self):
        return super(RoomTypeManager, self).get_queryset().filter(type=2)

    def triple_rooms(self):
        return super(RoomTypeManager, self).get_queryset().filter(type=3)

    def quad_rooms(self):
        return super(RoomTypeManager, self).get_queryset().filter(type=4)


class RoomStatusManager(models.Manager):
    def reserved_rooms(self):
        return super(RoomStatusManager, self).get_queryset().filter(status=True)

    def free_rooms(self):
        return super(RoomStatusManager, self).get_queryset().filter(status=False)


# Create your models here.
class Room(models.Model):
    TYPE = (
        (1, 'Single'),
        (2, 'Double'),
        (3, 'Triple'),
        (4, 'Quad')
    )
    room_number = models.CharField(max_length=10000)
    room_description = models.CharField(max_length=300, default="Description")
    type = models.IntegerField(choices=TYPE, default=1)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    status = models.BooleanField(default=False)
    price = models.IntegerField(default=10000)

    rooms_by_types = RoomTypeManager()
    rooms_by_status = RoomStatusManager()
    objects = RoomManager()

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.room_number
