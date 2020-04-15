from django.conf.urls import include, url

from rest_framework import routers

from .views import ObjectViewSet

router = routers.DefaultRouter()
router.register(r"objects", ObjectViewSet)

urlpatterns = [url("v1/", include([url("", include(router.urls))]),)]
