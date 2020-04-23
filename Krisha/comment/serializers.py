from rest_framework import serializers
from .models import Comment
from hotel.serializers import HotelShortSerializer
from auth_.serializers import MyUserSerializer

class CommentSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=300)
    created_date = serializers.DateTimeField(required=False)
    hotel = HotelShortSerializer(read_only=True)
    user = MyUserSerializer(read_only=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.created_date = validated_data.get('created_date',instance.created_date)
        instance.hotel = validated_data.get('hotel', instance.hotel)
        instance.save()
        return instance
