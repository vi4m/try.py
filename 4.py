#!/usr/bin/python
# coding: utf-8

import unittest
import re


class ServersList(object):

    def __init__(self, filename):
        self.filename = filename

    def filter(self):
        with open(self.filename, "r") as f:
            for line in f:
                hostname, ip, venture = line.split(":")
                if re.match("[a-zA-Z][0-9]+", hostname):
                    yield hostname


class LoggerTest(unittest.TestCase):

    def setUp(self):
        self.servers_list = ServersList(filename="/tmp/input")

    def testLog(self):
        example = "s10335.dc2:127.0.0.1:venture1\ns10448.dc2:127.0.0.1:venture2\nxxxxxx:xxxxx:xxxxx\nyyyyy:yyyyy:yyyyy"  # noqa
        with open("/tmp/input", "w") as f:
            f.write(example)
        result = self.servers_list.filter()
        self.assertEqual(list(result), ["s10335.dc2", "s10448.dc2"])
