#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

import django_filters

from .models import Group, Userprofile


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'id': ['exact'],
        }


class UserprofileFilter(django_filters.FilterSet):
    class Meta:
        model = Userprofile
        fields = {
            'user_id': ['exact'],
        }
