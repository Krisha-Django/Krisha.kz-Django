from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from auth_ import views
from .views import UserViewSet, ProfileViewSet

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('profiles', ProfileViewSet, basename='profiles')
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.MyUserAPIView.as_view())
]

urlpatterns += router.urls
