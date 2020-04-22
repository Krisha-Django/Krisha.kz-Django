from rest_framework import serializers
from .models import Hotel
from city.serializers import CitySerializer


class HotelSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'description', 'type_by_size',
                  'type_by_location', 'type_by_target', 'type_by_star', 'city', 'address', 'image', 'contact')
