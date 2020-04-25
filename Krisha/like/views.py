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

