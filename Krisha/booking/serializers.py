from rest_framework import serializers
from .models import Reservation
from Room.serializers import RoomSerializer


class CitySerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = ('reservation_id', 'guest_id', 'hotel_id', 'room_type', 'start_date', 'end_date', 'room')
