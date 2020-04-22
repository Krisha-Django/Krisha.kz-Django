from django.urls import path
from .views import HotelView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', HotelView, basename="hotels")
urlpatterns = router.urls
