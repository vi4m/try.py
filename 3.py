#!/usr/bin/python
# coding: utf-8

import unittest


# write solution here


class DoogieTest(unittest.TestCase):

    def setUp(self):
        self.logger = Doogie()

    def testLog(self):
        example = "sometest"
        self.logger.log(example)
        self.assertEquals(open("/tmp/output", "r").read(), example)
