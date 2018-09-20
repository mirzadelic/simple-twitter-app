from django.urls import path, include
from rest_framework import routers

from .views import PostView


router = routers.DefaultRouter()
router.register('post', PostView)

app_name = 'post'
urlpatterns = [
    path('', include(router.urls)),
]
