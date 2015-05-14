# -*- coding: utf-8 -*-
from rest_framework_3.response import Response
from rest_framework_3.viewsets import ModelViewSet

from rest_framework_extensions_3.mixins import NestedViewSetMixin
from rest_framework_extensions_3.decorators import action, link

from .models import (
    DefaultRouterUserModel,
    DefaultRouterGroupModel,
    DefaultRouterPermissionModel,
)


class UserViewSet(NestedViewSetMixin, ModelViewSet):
    model = DefaultRouterUserModel


class GroupViewSet(NestedViewSetMixin, ModelViewSet):
    model = DefaultRouterGroupModel


class PermissionViewSet(NestedViewSetMixin, ModelViewSet):
    model = DefaultRouterPermissionModel