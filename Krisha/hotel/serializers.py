from rest_framework import serializers
from .models import Hotel
from city.serializers import CitySerializer


# class HotelSerializer(serializers.ModelSerializer):
#     city = CitySerializer(read_only=True)
#
#     class Meta:
#         model = Hotel
#         fields = ('id', 'name', 'description', 'type_by_size',
#                   'type_by_location', 'type_by_target', 'type_by_star', 'city', 'address', 'image', 'contact')


class HotelShortSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'type_by_star')


class HotelFullSerializer(HotelShortSerializer):
    city = CitySerializer(read_only=True)
    description = serializers.CharField(required=False)
    contact = serializers.CharField(required=False)

    class Meta(HotelShortSerializer.Meta):
        fields = HotelShortSerializer.Meta.fields + ('description', 'type_by_size', 'type_by_location',
                                                     'type_by_target', 'city', 'address', 'image', 'contact')
