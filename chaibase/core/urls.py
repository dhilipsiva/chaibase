#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: urls.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-06-07
"""

from django.conf.urls import url
from chaibase.core.views import login, check, logout, browser, user

urlpatterns = [
    url(r'^login$', login, name="login"),
    url(r'^check$', check, name="check"),
    url(r'^logout$', logout, name="logout"),
    url(r'^browser/([a-z0-9]{32})$', browser, name="browser"),
    url(r'^users/([\-a-z0-9]{36})$', user, name="user"),
]
