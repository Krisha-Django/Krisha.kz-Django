from rest_framework import serializers
from auth_.models import MyUser, Profile
from city.serializers import CitySerializer


class MyUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'role', 'email', 'birthday', 'mobile', "first_name", 'last_name', 'is_admin')

    def create(self, validated_data):
        user = MyUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'city', 'card_number')


class ProfileGetSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'city', 'card_number')
