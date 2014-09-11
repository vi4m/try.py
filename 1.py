#!/usr/bin/python
# coding: utf-8

import unittest


def sum_(x, y):
    return x+y


class SumTest(unittest.TestCase):

    def setUp(self):
        pass

    def testSum(self):
        self.assertEquals(sum_(1, 99), 100)
