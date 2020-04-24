from rest_framework import serializers
from .models import Room
from hotel.serializers import HotelFullSerializer, HotelShortSerializer


class RoomShortSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField(required=False)
    class Meta:
        model = Room
        fields = ('id', 'room_number', 'type', 'status', 'price')


class RoomFullSerializer(RoomShortSerializer):
    hotel = HotelShortSerializer(read_only=True)

    class Meta(RoomShortSerializer.Meta):
        fields = RoomShortSerializer.Meta.fields + ('hotel', 'room_description',)
