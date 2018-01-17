#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="url-permission",
    version="0.0.1",
    author="ttxsgoto",
    author_email="359450323@qq.com",
    description="A simple Django app permission",
    long_description=README,
    url="git@github.com:ttxsgoto/url_permission.git",
    install_requires=[
        "djangorestframework==3.7.1",
        "django-filters==0.2.1",
        "django-rest-swagger==2.1.2",
    ],
    packages=find_packages(),
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)


