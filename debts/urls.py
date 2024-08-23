from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DebtsViewSet

router = DefaultRouter()
router.register(r'debts', DebtsViewSet, basename='debts')

debts_urlpatterns = [
    path('', include(router.urls)),
]