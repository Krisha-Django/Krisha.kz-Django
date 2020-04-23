from django.urls import path
from .views import ReservationView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', ReservationView, basename="rooms")
urlpatterns = router.urls

