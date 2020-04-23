from rest_framework import serializers
from .models import Comment
from hotel.serializers import HotelShortSerializer
from auth_.serializers import MyUserSerializer


class CommentShortSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=False)
    created_date = serializers.DateTimeField(required=False)

    class Meta:
        model = Comment
        fields = ('id','text','created_date')


class CommentFullSerializer(CommentShortSerializer):
    hotel = HotelShortSerializer(read_only=True)
    user = MyUserSerializer(read_only=True)

    class Meta(HotelShortSerializer.Meta):
        fields = CommentShortSerializer.Meta.fields + ('user', 'hotel')