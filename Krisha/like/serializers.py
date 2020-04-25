from rest_framework import serializers
from .models import Like
from hotel.serializers import HotelShortSerializer
from auth_.serializers import MyUserSerializer


class LikeSerializer(serializers.Serializer):
    hotel = HotelShortSerializer(read_only=True)
    user = MyUserSerializer(read_only=True)

    def create(self, validated_data):
        return Like.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.hotel = validated_data.get('hotel', instance.hotel)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance

