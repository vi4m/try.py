#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

import mock

import ocp.xyz
from os.library import db

CONST = 10
CONST_2 = 20


class MyAppUnknownError(Exception):
    pass


class MyApp(object):
    """This is my app"""
    def __init__(self, *args, **kwargs):
        print("Wow")

    def do_something(self):
        print("Something!")


MyApp().do_something()
