# -*- coding: utf-8 -*-
import django_filters
from rest_framework_3 import viewsets
from rest_framework_3 import filters
from rest_framework_3.permissions import DjangoModelPermissions
from rest_framework_extensions_3.mixins import ListUpdateModelMixin

from .models import (
    CommentForListUpdateModelMixin as Comment,
    UserForListUpdateModelMixin as User
)
from .serializers import UserSerializer, CommentSerializer


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = [
            'id'
        ]


class CommentViewSet(ListUpdateModelMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CommentFilter


class CommentViewSetWithPermissions(CommentViewSet):
    permission_classes = (DjangoModelPermissions,)


class UserViewSet(ListUpdateModelMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer