#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from .views import URLSourceViewSet, GroupViewSet, UserprofileViewSet

urlpatterns = [
    # permission
    url('^url/$', URLSourceViewSet.as_view({'get': 'list',})),
    url('^group/$', GroupViewSet.as_view({'get': 'list', 'post': 'create'})),
    url('^group/(?P<pk>\w+)/$', GroupViewSet.as_view({'put': 'update'})),
    url('^user_permission/$', UserprofileViewSet.as_view({'get': 'list'})),
    url('^user_permission/(?P<pk>\w+)$', UserprofileViewSet.as_view({'put': 'update'})),
]
