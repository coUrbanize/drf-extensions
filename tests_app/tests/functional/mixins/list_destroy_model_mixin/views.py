# -*- coding: utf-8 -*-
import django_filters
from rest_framework_3 import viewsets, serializers
from rest_framework_3 import filters
from rest_framework_3.permissions import DjangoModelPermissions
from rest_framework_extensions_3.mixins import ListDestroyModelMixin

from .models import CommentForListDestroyModelMixin as Comment


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = [
            'id'
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment


class CommentViewSet(ListDestroyModelMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CommentFilter


class CommentViewSetWithPermissions(CommentViewSet):
    permission_classes = (DjangoModelPermissions,)