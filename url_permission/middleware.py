#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import json
from collections import Counter
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from .models import Userprofile
from django.contrib.auth import get_user_model
from .settings import url_permisson_settings

logs = logging.getLogger('django')

User = get_user_model()


class URLPermissionMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        response = {
            "status_code": 403,
            "message": u"无权限操作,请联系管理员."
        }
        path = request.path.split('/')
        if path[1] in url_permisson_settings.ALL_ALLOW_URL:
            return None
        if not isinstance(request.user, User):
            return None
        if request.user.is_superuser:
            return None
        try:
            profile = Userprofile.objects.get(user=request.user)
        except Userprofile.DoesNotExist:
            return HttpResponseForbidden(json.dumps(response), content_type='application/json')
        method = request.method.lower()
        path = request.path.strip()
        if method == 'get':
            parameter = []
            for _parameter in request.GET.items():
                parameter.append(_parameter[0])
        else:
            try:
                parameter_dict = json.loads(request.body)
            except Exception:
                parameter_dict = {}
            parameter = parameter_dict.keys()
        all_permission = profile.get_all_permissions()
        result = None
        for _url in all_permission:
            url = _url.url
            action = _url.action
            parameters = _url.parameters.split(',')
            if method == action and path == url and (len(Counter(parameter) - Counter(parameters)) == 0):
                result = True
        if not result:
            return HttpResponseForbidden(json.dumps(response), content_type='application/json')
        return None
