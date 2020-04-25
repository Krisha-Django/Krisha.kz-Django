from rest_framework import serializers
from .models import Room
from hotel.serializers import HotelFullSerializer, HotelShortSerializer
from .validators import validated_price, validated_room_number


class RoomShortSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField(required=False, validators=[validated_room_number])
    price = serializers.IntegerField(required=False, validators=[validated_price])

    class Meta:
        model = Room
        fields = ('id', 'room_number', 'type', 'status', 'price')


class RoomFullSerializer(RoomShortSerializer):
    hotel = HotelShortSerializer(read_only=True)

    class Meta(RoomShortSerializer.Meta):
        fields = RoomShortSerializer.Meta.fields + ('hotel', 'room_description',)

class RoomPostPutSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField(required=False)
    room_description = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)

    class Meta:
        model = Room
        fields = '__all__'
