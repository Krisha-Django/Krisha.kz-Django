from rest_framework import serializers
from .models import Room
from hotel.serializers import HotelSerializer


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ('room_id', 'type', 'hotel','quest_id','reservation_id','status','status','price')

