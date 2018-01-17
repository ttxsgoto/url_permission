#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import URLSource, UserURL, Userprofile, Group, GroupURL, UserGroup


class UserprofileListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    group_permission = serializers.SerializerMethodField('_get_group_permission')
    user_permission = serializers.SerializerMethodField('_get_user_permission')
    all_permission = serializers.SerializerMethodField('_get_all_permission')

    class Meta:
        model = Userprofile
        fields = (
            'user', 'username', 'sex', 'desc', 'group_permission', 'user_permission', 'all_permission', 'create_time')

    def _get_group_permission(self, obj):
        group_permission = obj.get_group_permissions() if obj else []
        return UserGroupSerializer(group_permission, many=True).data if group_permission else []

    def _get_user_permission(self, obj):
        user_permission = obj.get_url_permissions() if obj else []
        return UserURLSerializer(user_permission, many=True).data if user_permission else []

    def _get_all_permission(self, obj):
        all_permission = obj.get_all_permissions() if obj else []
        return URLSourceSerializer(all_permission, many=True).data if all_permission else []


class UserprofileSerializer(serializers.ModelSerializer):
    permission = serializers.CharField(max_length=1024, allow_blank=True, required=False, help_text=u'权限id,逗号分隔')
    group = serializers.CharField(max_length=32, allow_blank=True, required=False, help_text=u'权限组id')

    class Meta:
        model = Userprofile
        fields = ('user', 'permission', 'group',)
        read_only_fields = ('user',)

    def save(self, **kwargs):
        permission = self.validated_data.pop('permission')
        group = self.validated_data.pop('group')
        instance = super(UserprofileSerializer, self).save(**kwargs)
        if permission:
            id_list = [int(id) for id in permission.strip().split(',')]
            permission_list = URLSource.objects.filter(id__in=id_list)
            instance.add_permissions(list(permission_list))
        if group:
            group = Group.objects.filter(id=group).first()
            instance.add_groups(group)
        return instance


class URLSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLSource
        fields = '__all__'


class UserURLSerializer(serializers.ModelSerializer):
    url_name = serializers.CharField(source='url.description')
    url_url = serializers.CharField(source='url.url')

    class Meta:
        model = UserURL
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    permission = serializers.CharField(max_length=1024, allow_blank=True, required=False, help_text=u'权限id,逗号分隔')
    group_permission = serializers.SerializerMethodField('_get_group_permission')

    class Meta:
        model = Group
        fields = ('id', 'name', 'permission', 'group_permission')

    def _get_group_permission(self, obj):
        all_permission = obj.get_group_permissions()
        return GroupURLSerializer(list(all_permission), many=True).data if all_permission else []

    def save(self, **kwargs):
        permission = self.validated_data.pop('permission')
        if not permission:
            return super(GroupSerializer, self).save(**kwargs)
        id_list = [int(id) for id in permission.strip().split(',')]
        permission_list = URLSource.objects.filter(id__in=id_list)
        instance = super(GroupSerializer, self).save(**kwargs)
        instance.add_permissions(list(permission_list))
        return instance


class UserGroupSerializer(serializers.ModelSerializer):
    permission = serializers.SerializerMethodField('_get_group_permission')

    class Meta:
        model = UserGroup
        fields = '__all__'

    def _get_group_permission(self, obj):
        all_permission = obj.group.get_group_permissions() if obj.group else []
        return GroupURLSerializer(list(all_permission), many=True).data if all_permission else []


class GroupURLSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name')
    url_name = serializers.CharField(source='url.description')
    url_url = serializers.CharField(source='url.url')

    class Meta:
        model = GroupURL
        fields = '__all__'
