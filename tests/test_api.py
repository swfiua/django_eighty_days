#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_eighty_days
------------

Tests for `django_eighty_days` api module.
"""

import os
import shutil
import unittest
import doctest

from django_eighty_days import api


class TestDjango_eighty_days(unittest.TestCase):

    def setUp(self):
        pass

    def test_doctests(self):
        """ Do doctests """
        doctest.testmod(api)

    def tearDown(self):
        pass
