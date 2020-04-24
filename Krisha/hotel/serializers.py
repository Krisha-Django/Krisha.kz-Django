from rest_framework import serializers
from .models import Hotel
from city.serializers import CitySerializer
from .validators import validate_name, validated_image
from city.models import City


class HotelShortSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False,validators=[validate_name])
    image = serializers.ImageField(required=False,validators=[validated_image])

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'type_by_star', 'image')


class HotelFullSerializer(HotelShortSerializer):
    city = CitySerializer(read_only=True)
    description = serializers.CharField(required=False)
    contact = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    class Meta(HotelShortSerializer.Meta):
        fields = HotelShortSerializer.Meta.fields + ('description', 'type_by_size', 'type_by_location',
                                                     'type_by_target', 'city', 'address', 'contact')

    # def create(self, validated_data):
    #     city = validated_data.pop('city')
    #     ccity = City()
    #     ccity.id = city['id']
    #     ccity.name = city['name']
    #     hotel = Hotel.objects.create(city=ccity,**validated_data)
    #     return hotel
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.type_by_star = validated_data.get('type_by_star', instance.type_by_star)
    #     instance.type_by_size = validated_data.get('type_by_size', instance.type_by_size)
    #     instance.type_by_location = validated_data.get('type_by_location', instance.type_by_location)
    #     instance.type_by_target = validated_data.get('type_by_target', instance.type_by_target)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.contact = validated_data.get('contact', instance.contact)
    #     instance.save()
    #     return instance
