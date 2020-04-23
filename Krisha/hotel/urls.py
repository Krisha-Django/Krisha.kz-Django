from django.urls import path
from .views import HotelView, HotelRoomsAPIView, HotelCommentsAPIView, HotelLikesAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', HotelView, basename="hotels")

urlpatterns = [
    path('<int:pk>/rooms/', HotelRoomsAPIView.as_view()),
    path('<int:pk>/comments/', HotelCommentsAPIView.as_view()),
    path('<int:pk>/likes/', HotelLikesAPIView.as_view()),
]
urlpatterns += router.urls
