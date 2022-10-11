from django.http import JsonResponse, HttpResponse
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'serializer', views.TaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/serializer/players/', views.user_playtime),
]