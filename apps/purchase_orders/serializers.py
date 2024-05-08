from rest_framework import serializers

from apps.purchase_orders.models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = (
            'id',
            'po_number',
            'vendor',
            'order_date',
            'delivery_date',
            'quantity',
            'items',
            'status',
            'quality_rating',
            'issue_date',
            'acknowledgment_date'
        )
