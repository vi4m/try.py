#!/usr/bin/python
# coding: utf-8

import unittest


class Logger:
    def log(self, s):
        with open("/tmp/output", "w+") as f:
            f.write(s)


class LoggerTest(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def testLog(self):
        example = "sometest"
        self.logger.log(example)
        self.assertEquals(open("/tmp/output", "r").read(), example)
