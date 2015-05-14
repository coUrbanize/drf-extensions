# -*- coding: utf-8 -*-
from rest_framework_3 import viewsets
from rest_framework_extensions_3.etag.mixins import ListETAGMixin, RetrieveETAGMixin
from rest_framework_3.filters import DjangoFilterBackend

from .models import KeyConstructorUserModel as UserModel
from .serializers import UserModelSerializer


class UserModelViewSet(ListETAGMixin, RetrieveETAGMixin, viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('property',)