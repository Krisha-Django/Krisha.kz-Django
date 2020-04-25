from rest_framework import serializers
from .models import Hotel
from city.serializers import CitySerializer
from .validators import validate_name, validated_image
from city.models import City


class HotelShortSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, validators=[validate_name])

    # image = serializers.ImageField(required=False, validators=[validated_image])

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'type_by_star',)


class HotelFullSerializer(HotelShortSerializer):
    city = CitySerializer(read_only=True, required=False)
    description = serializers.CharField(required=False)
    contact = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    class Meta(HotelShortSerializer.Meta):
        fields = HotelShortSerializer.Meta.fields + ('description', 'city', 'address', 'contact')


class HotelPostPutSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    contact = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    type_by_star = serializers.IntegerField(required=False)

    class Meta:
        model = Hotel
        fields = '__all__'
