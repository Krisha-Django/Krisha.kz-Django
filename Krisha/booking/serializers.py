from rest_framework import serializers
from .models import Reservation
from .models import Reservation
from ..room.serializers import RoomShortSerializer, RoomFullSerializer
from ..auth_.serializers import MyUserSerializer
from ..hotel.serializers import HotelFullSerializer


class ReservationShortSerializer(serializers.ModelSerializer):
    reservation_id = serializers.IntegerField(required=False)
    room = RoomFullSerializer()
    guest = MyUserSerializer()

    class Meta:
        model = Reservation
        fields = ('id', 'room', 'guest')


class ReservationFullSerializer(ReservationShortSerializer):
    hotel = HotelFullSerializer()

    class Meta(ReservationShortSerializer.Meta):
        fields = ReservationShortSerializer.Meta.fields + (
            'description', 'start_date', 'end_date', 'terminate', 'hotel')
