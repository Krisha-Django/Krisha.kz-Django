import logging

from django.shortcuts import render
from rest_framework import viewsets, status, mixins, decorators

from auth_.permissions import IsAdmin
from .serializers import RoomShortSerializer, RoomFullSerializer, RoomPostPutSerializer
from .models import Room


logger = logging.getLogger('like')
# Create your views here.


class RoomView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):

    permission_classes = (IsAdmin,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get('pk'):
                return RoomFullSerializer
            return RoomShortSerializer
        else:
            return RoomPostPutSerializer

    def get_queryset(self):
        # print(self.request.user.role)
        if self.request.user.role == 1:
            return Room.objects.all()
        else:
            type_ = self.request.query_params.get('type', None)
            rooms = Room.rooms_by_status.free_rooms()
            if type_ == '1':
                rooms = rooms.filter(type=1)
            elif type_ == '2':
                rooms = rooms.filter(type=2)
            elif type_ == '3':
                rooms = rooms.filter(type=3)
            elif type_ == '4':
                rooms = rooms.filter(type=4)
            return rooms.filter(status=False)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            room_number = serializer.data['room_number']
            hotel_id = serializer.data['hotel']
            logger.info(f'Room with number = {room_number} is created in hotel with id = {hotel_id} ')

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            room_id = serializer['id'].value
            logger.info(f'Room with id={room_id} was updated')

    def perform_destroy(self, instance):
        room_id = self.kwargs['pk']
        instance.delete()
        logger.info(f'Room with id={room_id} was deleted')
