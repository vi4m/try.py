#!/usr/bin/python
# coding: utf-8

import unittest


# write here solution

class SumTest(unittest.TestCase):

    def setUp(self):
        pass

    def testSum(self):
        self.assertEquals(
            capitalize(["raz", "dwa", "trzy"]), ["Raz", "Dwa", "Trzy"]
        )

    def testEmpty(self):
        with self.assertRaises(TypeError):
            capitalize([])
