#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import argparse
import unittest
import subprocess


def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check quiz')
    parser.add_argument('task', metavar='task', type=str)
    parser.add_argument('--hard', metavar='hard', type=bool)

    args = parser.parse_args()
    task = args.task
    hard = args.hard
    if not which("flake8"):
        print("flake8 missing")
        sys.exit(1)

    if ".py" in task:
        task = task.replace(".py", "")
    task = int(task)
    suite = unittest.TestSuite()
    style_result = test_result = None

    try:
        print("Style checking....")
        style_result = subprocess.check_call(
            "flake8 %s.py 1>&2" % task, shell=True)
    except subprocess.CalledProcessError:
        pass
        # print("Style check failed, fix errors!")

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
