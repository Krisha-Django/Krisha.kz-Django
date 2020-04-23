from django.urls import path
from .views import RoomView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', RoomView, basename="rooms")
urlpatterns = router.urls

