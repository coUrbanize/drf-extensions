# -*- coding: utf-8 -*-
from rest_framework_3 import routers

from .views import CommentViewSet, CommentViewSetWithPermissions


viewset_router = routers.DefaultRouter()
viewset_router.register('comments', CommentViewSet)
viewset_router.register('comments-with-permissions', CommentViewSetWithPermissions)
urlpatterns = viewset_router.urls