from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from .serializers import ReservationShortSerializer, ReservationFullSerializer,ReservationSerializer
from .models import Reservation


# Create your views here.


class ReservationView(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get('pk'):
                return ReservationFullSerializer
            return ReservationShortSerializer
        else:
            return ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.all()
