from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import HotelFullSerializer, HotelShortSerializer
from .models import Hotel
# Create your views here.


class HotelView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

    # permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get('pk'):
                return HotelFullSerializer
            return HotelShortSerializer
        else:
            return HotelFullSerializer

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
