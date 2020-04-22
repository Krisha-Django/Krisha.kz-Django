
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from auth_ import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.MyUserAPIView.as_view())
]


