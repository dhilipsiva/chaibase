#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: enums.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-05-27
"""

from orm_choices import choices_with_unknown as choices


@choices
class EntryGrade:
    class Meta:
        A = [1, "A"]
        A_PLUS = [2, "A+"]
        B = [3, "B"]
        B_PLUS = [4, "B+"]
        C = [5, "C"]


@choices
class DeductionReason:
    class Meta:
        WATER = [1, "Water"]
        STICK = [2, "Stick"]
        TARE = [3, "Tare"]
        BURNT = [4, "Burnt"]
        COARSE = [5, "Coarse"]
        TEA = [6, "Tea"]
        OTHERS = [7, "Others"]


@choices
class StaffRole:
    class Meta:
        ADMIN = [1, "Admin"]
        MANAGER = [2, "Manager"]
        SUPERVISOR = [3, "Supervisor"]
        WRITER = [4, "Writer"]
        INSPECTOR = [5, "Inspector"]
