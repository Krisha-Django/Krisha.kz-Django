from rest_framework import serializers
from .models import Room
from hotel.serializers import HotelFullSerializer


class RoomShortSerializer(serializers.ModelSerializer):
    room_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Room
        fields = ('room_id', 'type', 'status', 'price')


class RoomFullSerializer(RoomShortSerializer):
    hotel = HotelFullSerializer(read_only=True)

    class Meta(RoomShortSerializer.Meta):
        fields = RoomShortSerializer.Meta.fields + ('hotel', 'quest_id', 'reservation_id')
