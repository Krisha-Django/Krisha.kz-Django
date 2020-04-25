from django.http import Http404
from rest_framework import viewsets, status, mixins, generics
from rest_framework.permissions import IsAuthenticated

from auth_.permissions import IsAdmin
from .serializers import HotelFullSerializer, HotelShortSerializer,HotelPostPutSerializer
from room.serializers import RoomFullSerializer, RoomShortSerializer
from comment.serializers import CommentFullSerializer, CommentShortSerializer
from like.serializers import LikeSerializer,LikeFullSerializer
from .models import Hotel


# Create your views here.


class HotelView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    permission_classes = (IsAdmin,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get('pk'):
                return HotelFullSerializer
            return HotelShortSerializer
        else:
            return HotelPostPutSerializer

    def get_queryset(self):

        star_number = self.request.query_params.get('type_by_star', None)

        if star_number == '1':
            return Hotel.by_stars_objects.one_starred_hotels()
        elif star_number == '2':
            return Hotel.by_stars_objects.two_starred_hotels()
        elif star_number == '3':
            return Hotel.by_stars_objects.three_starred_hotels()
        elif star_number == '4':
            return Hotel.by_stars_objects.four_starred_hotels()
        elif star_number == '5':
            return Hotel.by_stars_objects.five_starred_hotels()
        else:
            return Hotel.objects.all()


class HotelRoomsAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAdmin,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RoomShortSerializer
        else:
            return RoomFullSerializer

    def get_queryset(self):
        try:
            hotel = Hotel.objects.get(id=self.kwargs['pk'])
        except Hotel.DoesNotExist:
            raise Http404
        return hotel.rooms.all()




class HotelCommentsAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentShortSerializer
        else:
            return CommentFullSerializer

    def get_queryset(self):
        try:
            hotel = Hotel.objects.get(id=self.kwargs['pk'])
        except Hotel.DoesNotExist:
            raise Http404
        return hotel.comments.all()


class HotelLikesAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return LikeFullSerializer

    def get_queryset(self):
        try:
            hotel = Hotel.objects.get(id=self.kwargs['pk'])
        except Hotel.DoesNotExist:
            raise Http404
        return hotel.likes.all()
