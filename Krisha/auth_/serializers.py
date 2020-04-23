from rest_framework import serializers
from auth_.models import MyUser, Profile


class MyUserSerializer(serializers.ModelSerializer):
    first_name = serializers.ModelSerializer(required=False)
    second_name = serializers.ModelSerializer(required=False)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'first_name', 'second_name')


class ProfileSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('user')
