from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from .serializers import RoomShortSerializer, RoomFullSerializer
from .models import Room

# Create your views here.


class RoomView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get('pk'):
                return RoomFullSerializer
            return RoomShortSerializer
        else:
            return RoomFullSerializer

    def get_queryset(self):
        type_ = self.request.query_params.get('type', None)
        if type_ == '1':
            return Room.rooms_by_types.single()
        elif type_ == '2':
            return Room.rooms_by_types.double_rooms()
        elif type_ == '3':
            return Room.rooms_by_types.triple_rooms()
        elif type_ == '4':
            return Room.rooms_by_types.quad_rooms()
        else:
            return Room.objects.all()
