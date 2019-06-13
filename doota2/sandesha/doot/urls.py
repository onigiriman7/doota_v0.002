from django.urls import path

from rest_framework import routers
from .api import PostViewSet

router = routers.DefaultRouter()
router.register('api', PostViewSet, 'api')

urlpatterns = router.urls