from datetime import datetime
import pytz
from django.core.exceptions import ValidationError

from .models import Reservation
from rest_framework import serializers
from room.serializers import RoomShortSerializer, RoomFullSerializer
from auth_.serializers import MyUserSerializer
from hotel.serializers import HotelFullSerializer, HotelShortSerializer


class ReservationShortSerializer(serializers.ModelSerializer):
    room = RoomShortSerializer(read_only=True)
    guest = MyUserSerializer(read_only=True)

    # description = serializers.CharField(max_length=300)

    class Meta:
        model = Reservation
        fields = ('id', 'description', 'guest', 'room')


class ReservationFullSerializer(ReservationShortSerializer):
    hotel = HotelShortSerializer(read_only=True)

    # validation for end_date
    class Meta(ReservationShortSerializer.Meta):
        fields = ReservationShortSerializer.Meta.fields + (
            'hotel', 'start_date', 'end_date', 'terminate', 'description')


class ReservationSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
    terminate = serializers.BooleanField(required=False)

    class Meta:
        model = Reservation
        fields = '__all__'
