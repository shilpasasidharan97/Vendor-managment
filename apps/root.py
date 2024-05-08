from collections import OrderedDict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):

    get_uri = lambda uri_name, *args, **kwargs: request.build_absolute_uri(
        reverse(uri_name, args=args, kwargs=kwargs, format=format))
    vendors = OrderedDict([
        # ('vendor.create', get_uri('vendor:vendors-list')),
        # ('features.disabled', get_uri('features.disabled')),
    ])
    api_endpoints = OrderedDict([
        ('vendors', vendors),
    ])
    return Response(api_endpoints)
