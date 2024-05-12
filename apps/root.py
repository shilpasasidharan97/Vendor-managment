from collections import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    get_uri = lambda uri_name, *args, **kwargs: request.build_absolute_uri(
        reverse(uri_name, args=args, kwargs=kwargs, format=format))

    vendors_endpoints = OrderedDict([
        ('list', get_uri('vendor:vendor-list')),
        ('create', get_uri('vendor:vendor-list')),
        ('retrieve', get_uri('vendor:vendor-detail', pk=1)),
        ('update', get_uri('vendor:vendor-detail', pk=1)),
        ('delete', get_uri('vendor:vendor-detail', pk=1)),
        ('performance', get_uri('vendor:vendor-performance', pk=1)),
    ])

    purchase_orders_endpoints = OrderedDict([
        ('list', get_uri('purchase_orders:purchaseorder-list')),
        ('create', get_uri('purchase_orders:purchaseorder-list')),
        ('retrieve', get_uri('purchase_orders:purchaseorder-detail', pk=1)),
        ('update', get_uri('purchase_orders:purchaseorder-detail', pk=1)),
        ('delete', get_uri('purchase_orders:purchaseorder-detail', pk=1)),
        ('acknowledge', get_uri('purchase_orders:acknowledge-purchase-order', pk=1)),
    ])

    api_endpoints = OrderedDict([
        ('vendors', vendors_endpoints),
        ('purchase_orders', purchase_orders_endpoints),
    ])

    return Response(api_endpoints)
