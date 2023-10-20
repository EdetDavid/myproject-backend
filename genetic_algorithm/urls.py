from django.urls import path, include
from .views import Individuals, UserViewSet
from .views import *
from rest_framework.routers import DefaultRouter


# url for viewsets using router
router = DefaultRouter()
router.register('users', UserViewSet, )
router.register('contact', ContactViewSet, )

urlpatterns = [
    path('api/individuals', Individuals.as_view(), name="individuals"),
    path('api/', include(router.urls)),
]

