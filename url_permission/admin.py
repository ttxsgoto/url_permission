#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from .models import Userprofile, URLSource, Group, UserGroup, UserURL, GroupURL


class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'desc', 'create_time')


class URLSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'action', 'parameters', 'description')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code',)


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'desc')


class UserURLAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'url', 'desc')


class GroupURLAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'url', 'desc')


admin.site.register(Userprofile, UserprofileAdmin)
admin.site.register(URLSource, URLSourceAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
admin.site.register(UserURL, UserURLAdmin)
admin.site.register(GroupURL, GroupURLAdmin)
