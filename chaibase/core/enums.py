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
class LeafGrade:
    class Meta:
        A = [1, "A"]
        A_PLUS = [2, "A+"]
        B = [3, "B"]
        B_PLUS = [4, "B+"]
        C = [5, "C"]
