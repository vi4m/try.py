#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import unittest
import subprocess

parser = argparse.ArgumentParser(description='Check quiz')
parser.add_argument('task', metavar='task', type=str)
parser.add_argument('hard', metavar='hard', type=str)

args = parser.parse_args()
task = args.task
hard = args.hard

if ".py" in task:
    task.replace(".py", "")
task = int(task)
suite = unittest.TestSuite()
style_result = test_result = None

try:
    print("Style checking....")
    style_result = subprocess.check_call(
        "flake8 %s.py 1>&2" % task, shell=True)
except subprocess.CalledProcessError:
    pass
    #print("Style check failed, fix errors!")

try:
    print("Unit test checking....")
    test_result = subprocess.check_call(
        "nosetests -s %s.py" % task, shell=True)
except subprocess.CalledProcessError:
    print("Unit test failed. Please fix errors!")

print("-" * 80)
if (test_result == 0):
    print("Great job!")

if hard:
    if style_result != 0:
        print("Not compatible with pep8.")
    else:
        print("Yeah. Compatible with pep8.")
    print("-"*80)
