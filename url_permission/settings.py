#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'URL_PERMISSION', [])

DEFAULTS = {
    'ALL_ALLOW_URL': ['docs', 'admin', 'api-auth']  # 不用检查url权限认证的url开头命名
}

url_permisson_settings = APISettings(USER_SETTINGS, DEFAULTS, None)
