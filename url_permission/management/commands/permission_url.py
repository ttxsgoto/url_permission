#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from django.core.management.base import BaseCommand, CommandError
from rest_framework.schemas import SchemaGenerator
from url_permission.models import URLSource


class GetURLSchemaGenerator(SchemaGenerator):
    def get_schema(self, request=None, public=False):
        if self.endpoints is None:
            inspector = self.endpoint_inspector_cls(self.patterns, self.urlconf)
            self.endpoints = inspector.get_api_endpoints()
        return self.get_links(None if public else request)

    def get_links(self, request=None):
        paths = []
        view_endpoints = []
        for path, method, callback in self.endpoints:
            view = self.create_view(callback, method, request)
            if getattr(view, u'exclude_from_schema', False):
                continue
            path = self.coerce_path(path, method, view)
            paths.append(path)
            view_endpoints.append((path, method, view))
        i = 0
        for path, method, view in view_endpoints:
            link = view.schema.get_link(path, method, base_url=self.url)
            parameters = []
            for field in link.fields:
                parameters.append(field[0])
            result = URLSource.objects.get_or_create(
                url=link.url,
                action=link.action,
                description=link.description,
                parameters=','.join(parameters)
            )
            if result[1]:
                i += 1
        return i


class Command(BaseCommand):
    help = u'添加URL信息到数据库中'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    # def add_arguments(self, parser):
    #     parser.add_argument('data_type', type=str, choices=['all', 'article', 'tag', 'category'],
    #                         help='article : all article,tag : all tag,category: all category,all: All of these')

    def handle(self, *args, **options):
        # print 'hello, django!', options['data_type']
        print u'添加新增URL信息到数据库中'
        generator = GetURLSchemaGenerator(
            title=None,
            url=None,
            patterns=None,
            urlconf=None,
            description=None
        )
        num = generator.get_schema(request=None)
        self.stdout.write(u'Successfully Add URL {} 条'.format(num))
