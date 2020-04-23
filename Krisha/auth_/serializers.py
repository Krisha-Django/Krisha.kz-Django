from rest_framework import serializers
from auth_.models import MyUser, Profile


class MyUserSerializer(serializers.ModelSerializer):
    first_name = serializers.ModelSerializer(required=True)
    second_name = serializers.ModelSerializer(required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'first_name', 'second_name')


class ProfileSerializer(serializers.ModelSerializer):
    user = MyUserSerializer()

    class Meta:
        model = Profile
        fields = ('user')
