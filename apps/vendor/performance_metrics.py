from datetime import datetime
from django.db.models import F
from apps.purchase_orders.models import PurchaseOrder
from .models import HistoricalPerformance


def recalculate_performance_metrics(vendor):
    completed_pos = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed')

    # On-Time Delivery Rate
    total_completed_pos = completed_pos.count()
    on_time_delivery_pos = completed_pos.filter(
        delivery_date__lte=F('acknowledgment_date')).count()
    vendor.on_time_delivery_rate = (
        on_time_delivery_pos / total_completed_pos) * 100 if total_completed_pos > 0 else 0

    # Quality Rating Average
    quality_ratings = completed_pos.exclude(
        quality_rating=None).values_list('quality_rating', flat=True)
    vendor.quality_rating_avg = sum(
        quality_ratings) / len(quality_ratings) if quality_ratings else 0

    # Average Response Time
    response_times = completed_pos.exclude(acknowledgment_date=None).annotate(
        response_time=F('acknowledgment_date') -
        F('issue_date')  # Use F object
    ).values_list('response_time', flat=True)
    total_response_time_seconds = sum(
        response_time.total_seconds() for response_time in response_times)
    average_response_time_seconds = total_response_time_seconds / \
        len(response_times) if response_times else 0
    vendor.average_response_time = average_response_time_seconds

    # Fulfillment Rate
    total_pos = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_pos = completed_pos.exclude(issue_date=None).count()
    vendor.fulfillment_rate = (
        fulfilled_pos / total_pos) * 100 if total_pos > 0 else 0
    vendor.save()

    # Saving data in historical performance of vendor
    HistoricalPerformance.objects.create(vendor=vendor, date=datetime.now(),
                                         on_time_delivery_rate=vendor.on_time_delivery_rate,
                                         quality_rating_avg=vendor.quality_rating_avg,
                                         average_response_time=vendor.average_response_time,
                                         fulfillment_rate=vendor.fulfillment_rate
                                         )
