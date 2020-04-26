import logging

from django.http import Http404
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from auth_.permissions import IsAdmin
from hotel.serializers import HotelFullSerializer, HotelShortSerializer

from .models import City
from .serializers import CitySerializer
from rest_framework.response import Response

logger = logging.getLogger('city')
# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAdmin, ])
def city_list(request, format=None):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            city_name = serializer.data['name']
            logger.info(f'City with name = {city_name} is created')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdmin, ])
def city_detail(request, pk, format=None):
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            city_name = serializer.data['name']
            logger.info(f'City with name = {city_name} is updated')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        city_id = city.id
        city.delete()
        logger.info(f'City with id = {city_id} is deleted')
        return Response(status=status.HTTP_204_NO_CONTENT)


class CityHotelsAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return HotelShortSerializer

    def get_queryset(self):
        try:
            city = City.objects.get(id=self.kwargs['pk'])
        except City.DoesNotExist:
            raise Http404
        return city.hotels.all()
