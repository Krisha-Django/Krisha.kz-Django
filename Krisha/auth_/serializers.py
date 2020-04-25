from rest_framework import serializers
from auth_.models import MyUser, Profile


class MyUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'role', 'email')

    def create(self, validated_data):
        user = MyUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'city', 'card_number')
