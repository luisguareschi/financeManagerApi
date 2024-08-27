from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DebtsViewSet, DebtorsViewSet

router = DefaultRouter()
router.register(r'debts', DebtsViewSet, basename='debts')
router.register(r'debtors', DebtorsViewSet, basename='debtors')

debts_urlpatterns = [
    path('', include(router.urls)),
]