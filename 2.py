#!/usr/bin/python
# coding: utf-8

import unittest


def capitalize(l):
    if not l:
        raise TypeError("You should define your list!")
    result = []
    for i in l:
        result.append(i.capitalize())
    return result


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
