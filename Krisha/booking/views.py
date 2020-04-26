import logging

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from .serializers import ReservationShortSerializer, ReservationFullSerializer, ReservationSerializer
from .models import Reservation

logger = logging.getLogger('reservation')


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
        if self.request.user.role == 2:
            return Reservation.objects.filter(guest=self.request.user)
        else:
            term = self.request.query_params.get('terminate')
            if term == 'true':
                return Reservation.objects.terminated()
            elif term == 'false':
                return Reservation.objects.in_use()
            else:
                return Reservation.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            user_id = serializer.data['guest']
            room_id = serializer.data['room']
            hotel_id = serializer.data['hotel']
            reservation_id = serializer['id'].value
            logger.info(
                f'Reservation with id={reservation_id} created: user_id= {user_id}. room_id={room_id}, hotel_id={hotel_id}')

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            reservation_id = serializer['id'].value
            logger.info(f'Reservation with id={reservation_id} was updated')

    def perform_destroy(self, instance):
        reservation_id = self.kwargs['pk']
        instance.delete()

        logger.info(f'Reservation with id={reservation_id} was deleted')
