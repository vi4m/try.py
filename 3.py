#!/usr/bin/python
# coding: utf-8

import unittest
import os


# write solution here

class LoggerTest(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def testLog(self):
        try:
            os.unlink("/tmp/output")
        except OSError:
            print("File doesn't exist, probably first run")

        example = "sometest"
        self.logger.log(example)
        self.logger.log(example)
        self.assertEquals(
            open("/tmp/output", "r").read(), example + "\n" + example + "\n")
