from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('content-detail', views.ContentViewset)
router.register('type-detail', views.TypeViewset)

urlpatterns = [
        path('', include(router.urls))
        ]
