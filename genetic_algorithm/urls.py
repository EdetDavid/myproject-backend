from django.urls import path, include

from .views import *
from rest_framework.routers import DefaultRouter


# url for viewsets using router
router = DefaultRouter()
router.register('users', UserViewSet, )


urlpatterns = [
    path('api/individuals/', Individuals.as_view(), name="individuals"),
    path('api/optimize/', Optimize.as_view(), name="optimize"),
    path('api/', include(router.urls)),
]
