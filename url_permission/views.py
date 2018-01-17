#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

from django.http import HttpResponse
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from .models import URLSource, UserURL, Userprofile, Group
from .serializers import URLSourceSerializer, UserURLSerializer, UserprofileSerializer, GroupSerializer, \
    UserprofileListSerializer
from .filters import GroupFilter, UserprofileFilter


class URLSourceViewSet(ModelViewSet):
    serializer_class = URLSourceSerializer
    queryset = URLSource.objects.all()

    def list(self, request, *args, **kwargs):
        """获取URL列表"""
        return super(URLSourceViewSet, self).list(request, *args, **kwargs)


class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    filter_class = GroupFilter

    def create(self, request, *args, **kwargs):
        """创建组和对应的权限"""
        return super(GroupViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """获取权限组对应的权限列表"""
        return super(GroupViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """更新权限组对应的权限"""
        return super(GroupViewSet, self).update(request, *args, **kwargs)


class UserprofileViewSet(ModelViewSet):
    serializer_class = UserprofileSerializer
    queryset = Userprofile.objects.all()
    filter_class = UserprofileFilter

    def get_serializer_class(self):
        """重写获取serializer class"""
        try:
            method = self.request.method
        except Exception:
            method = None
        if method and (method in SAFE_METHODS):
            return UserprofileListSerializer
        else:
            return self.serializer_class

    def list(self, request, *args, **kwargs):
        """获取用户对应的所有权限"""
        return super(UserprofileViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """用户添加组权限/单个权限"""
        group = request.data.get('group', '')
        permission = request.data.get('permission', '')

        if not group and not permission:
            return HttpResponse('参数错误.')
        return super(UserprofileViewSet, self).update(request, *args, **kwargs)
