from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DealerViewSet, CarViewSet

router = DefaultRouter()
router.register(r'dealer', DealerViewSet)
router.register(r'car', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]