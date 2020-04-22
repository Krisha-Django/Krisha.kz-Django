from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import  views

urlpatterns = [
    path('',views.city_list),
    path('<int:pk>/',views.city_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)