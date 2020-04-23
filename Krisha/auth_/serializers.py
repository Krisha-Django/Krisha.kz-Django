from rest_framework import serializers
from auth_.models import MyUser, Profile


class MyUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    class Meta:
        model = MyUser
        fields = ('username', 'is_super_man','email')


class ProfileSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('user','city','card_number')
