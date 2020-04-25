import logging

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from .models import Like
from .serializers import LikeSerializer, LikeFullSerializer

logger = logging.getLogger('like')
# Create your views here.
class LikeViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.request.method == "GET":
            return LikeFullSerializer
        else:
            return LikeSerializer

    def get_queryset(self):
            return Like.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            hotel_id = serializer.data['hotel']
            user_id = serializer.data['user']
            logger.info(f'User with id = {user_id} liked hotel with id = {hotel_id}')

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            like_id = serializer['id'].value
            logger.info(f'Like with id={like_id} was updated')

    def perform_destroy(self, instance):
        like_id = self.kwargs['pk']
        instance.delete()
        logger.info(f'Like with id={like_id} was deleted')
