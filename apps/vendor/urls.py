from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet

app_name = 'vendor'

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/performance/',
         VendorViewSet.as_view({'get': 'performance'}), name='vendor-performance'),
]
