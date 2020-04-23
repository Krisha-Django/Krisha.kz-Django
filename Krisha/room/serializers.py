from rest_framework import serializers
from .models import Room
from hotel.serializers import HotelFullSerializer


class RoomShortSerializer(serializers.ModelSerializer):
    room_number = serializers.IntegerField(read_only=True)

    class Meta:
        model = Room
        fields = ('room_number', 'type', 'status', 'price')


class RoomFullSerializer(RoomShortSerializer):
    hotel = HotelFullSerializer(read_only=True)

    class Meta(RoomShortSerializer.Meta):
        fields = RoomShortSerializer.Meta.fields + ('hotel', 'room_description',)
