from django.db import models
from hotel.models import Hotel


class RoomTypeManager(models.Manager):
    def single_rooms(self):
        super(RoomTypeManager, self).get_queryset().filter(type=1)

    def double_rooms(self):
        super(RoomTypeManager, self).get_queryset().filter(type=2)

    def triple_rooms(self):
        super(RoomTypeManager, self).get_queryset().filter(type=3)

    def quad_rooms(self):
        super(RoomTypeManager, self).get_queryset().filter(type=4)


class RoomStatusManager(models.Manager):
    def reserved_rooms(self):
        super(RoomStatusManager, self).get_queryset().filter(status=True)

    def free_rooms(self):
        super(RoomStatusManager, self).get_queryset().filter(status=False)


# Create your models here.
class Room(models.Model):
    TYPE = (
        (1, 'Single'),
        (2, 'Double'),
        (3, 'Triple'),
        (4, 'Quad')
    )
    room_id = models.IntegerField(primary_key=True)
    type = models.IntegerField(choices=TYPE, default=1)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    quest_id = models.IntegerField(null=True, blank=True)
    reservation_id = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    price = models.IntegerField(default=10000)

    rooms_by_types = RoomTypeManager()
    rooms_by_status = RoomStatusManager()

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'





