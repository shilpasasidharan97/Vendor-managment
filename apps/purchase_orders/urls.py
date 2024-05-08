from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PurchaseOrderViewSet

router = DefaultRouter()
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/acknowledge/', PurchaseOrderViewSet.as_view(
        {'post': 'acknowledge_purchase_order'}), name='acknowledge-purchase-order'),
]
