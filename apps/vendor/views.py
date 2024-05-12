from datetime import timezone
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from apps.vendor.models import Vendor
from apps.vendor.serializers import VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    # Custom method to handle vendor update with optional vendor_code
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        vendor_code = request.data.get('vendor_code', None)

        if vendor_code is not None:
            # If vendor_code is provided, proceed with the update including
            # vendor_code
            return super().update(request, *args, **kwargs)
        else:
            # If vendor_code is not provided, remove it from the request data
            request.data.pop('vendor_code', None)
            kwargs['partial'] = True
            return super().update(request, *args, **kwargs)

    # Custom action to retrieve performance metrics
    def performance(self, request, pk=None):
        vendor = self.get_object()
        performance_metrics = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return Response(performance_metrics)
