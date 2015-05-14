# -*- coding: utf-8 -*-
from rest_framework_3 import views
from rest_framework_3.response import Response

from rest_framework_extensions_3.cache.decorators import cache_response


class HelloView(views.APIView):
    @cache_response()
    def get(self, request, *args, **kwargs):
        return Response('Hello world')