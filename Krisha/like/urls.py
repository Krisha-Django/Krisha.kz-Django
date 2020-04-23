from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


router = DefaultRouter()

router.register(r'', views.LikeViewSet, basename="likes")


# urlpatterns = [
#     path('', views.LikeList.as_view()),
#     path('<int:pk>/', views.LikeDetail.as_view())
# ]
urlpatterns = router.urls
