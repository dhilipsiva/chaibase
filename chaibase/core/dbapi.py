#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: dbapi.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-05-27
"""

from chaibase.core.models import Person, Factory, Vehicle, Weighment, User, \
    Entry, Deduction, Browser


def get_person(**kwargs):
    """
    docstring for create_person
    """
    try:
        return Person.objects.get(**kwargs)
    except Person.DoesNotExist:
        return None


def create_person(**kwargs):
    """
    docstring for create_person
    """
    return Person.objects.create(**kwargs)


def get_factory(**kwargs):
    """
    docstring for get_factory
    """
    try:
        return Factory.objects.get(**kwargs)
    except Factory.DoesNotExist:
        return None


def create_factory(**kwargs):
    """
    docstring for create_person
    """
    return Factory.objects.create(**kwargs)


def get_vehicle(**kwargs):
    """
    docstring for get_factory
    """
    try:
        return Vehicle.objects.get(**kwargs)
    except Vehicle.DoesNotExist:
        return None


def create_vehicle(**kwargs):
    """
    docstring for create_person
    """
    return Vehicle.objects.create(**kwargs)


def get_weighment(**kwargs):
    """
    docstring for get_factory
    """
    try:
        return Weighment.objects.get(**kwargs)
    except Weighment.DoesNotExist:
        return None


def create_weighment(**kwargs):
    """
    docstring for create_person
    """
    return Weighment.objects.create(**kwargs)


def get_user(user_uuid):
    """
    docstring for get_factory
    """
    try:
        return User.objects.get(uuid=user_uuid)
    except User.DoesNotExist:
        return None

def get_user_by_username(username):
    """
    docstring for get_factory
    """
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None


def create_user(**kwargs):
    """
    docstring for create_user
    """
    return User.objects.create(**kwargs)


def get_entry(**kwargs):
    """
    docstring for get_entry
    """
    try:
        return Entry.objects.get(**kwargs)
    except Entry.DoesNotExist:
        return None


def create_entry(**kwargs):
    """
    docstring for create_entry
    """
    return Entry.objects.create(**kwargs)


def create_deduction(**kwargs):
    """
    docstring for create_entry
    """
    return Deduction.objects.create(**kwargs)


def get_browser(fingerprint):
    """
    Get a browser
    """
    try:
        return Browser.objects.get(fingerprint=fingerprint)
    except Browser.DoesNotExist:
        return None


def create_browser(fingerprint, data):
    """
    Create a browser
    """
    return Browser.objects.create(fingerprint=fingerprint, data=data)


def update_browser(browser, data):
    browser.data = data
    browser.save()
    return browser
