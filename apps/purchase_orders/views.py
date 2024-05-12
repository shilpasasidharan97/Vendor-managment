import datetime
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.purchase_orders.models import PurchaseOrder
from apps.purchase_orders.serializers import PurchaseOrderSerializer
from apps.vendor.performance_metrics import recalculate_performance_metrics


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def acknowledge_purchase_order(self, request, pk=None):
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)

        # Update acknowledgment_date
        purchase_order.acknowledgment_date = datetime.datetime.now()
        purchase_order.save()

        # Recalculate performance metrics for the vendor
        vendor = purchase_order.vendor
        recalculate_performance_metrics(vendor)

        return Response(
            {"message": "Purchase order acknowledged successfully"}, status=status.HTTP_200_OK)
