from rest_framework import generics, mixins, viewsets

from rest_framework.permissions import AllowAny, IsAuthenticated
from auth_.serializers import MyUserSerializer, ProfileSerializer, ProfileGetSerializer
from auth_.models import MyUser, Profile


class MyUserAPIView(generics.CreateAPIView, ):
    permission_classes = (AllowAny,)
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all()

    def perform_create(self, serializer):
        username = self.request.data.pop('username')
        password = self.request.data.pop('password')
        email = self.request.data.pop('email')
        firstname = self.request.data.pop('first_name')
        last_name = self.request.data.pop('last_name')
        role = self.request.data.pop('role')
        mobile = self.request.data.pop('mobile')

        user, created = MyUser.objects.get_or_create(username=username)
        user.email = email
        user.first_name = firstname
        user.last_name = last_name
        user.role = role
        user.mobile = mobile
        user.set_password(password)
        user.save()


class UserViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    def get_serializer_class(self):
        return MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all()


class ProfileViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProfileGetSerializer
        else:
            return ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()
