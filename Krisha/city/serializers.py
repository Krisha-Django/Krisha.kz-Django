from rest_framework import serializers
from .models import City


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return City.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

