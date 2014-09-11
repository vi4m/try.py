#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import ipaddress
import logging
import os
import sys
import subprocess


class InvalidIPError(Exception):
    pass


class Pinger(object):
    
    def __init__(self, low_ip, high_ip):
        if high_ip < low_ip:
            raise InvalidIPError("First IP should be lower than second")
        self.low_ip = low_ip
        self.high_ip = high_ip

    def ping_once(self, ip):
        """Span ping system command on given `ip` address"""
        subprocess.check_output("/usr/bin/ping", "-c", "1", str(ip))

    def __repr__(self):
        return "Pinger class from %s to %s" % (self.low_ip, self.high_ip)



# parse arguments
parser = argparse.ArgumentParser(description='Ping some IP ranges.')
parser.add_argument('low_ip', metavar='low_ip', type=str)
parser.add_argument('high_ip', metavar='high_ip', type=str)
args = parser.parse_args()
low_ip = ipaddress.ip_address(args.low_ip)
high_ip = ipaddress.ip_address(args.high_ip)

output_file = open("/tmp/output", "a")

current_ip = low_ip


while current_ip < high_ip:
    current_ip += 1
    print(current_ip)
    status = 0
    logging.debug("Pinging host: {}".format(current_ip))
    output_file.write("{} {} \n".format(current_ip, status))


def scan(ip):
    """Scan given ip address"""
    
#for ipaddress in ipaddress.ip_network('192.168.0.0/16').hosts():
#	print(ipaddress)
