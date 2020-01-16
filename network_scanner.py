#!/usr/bin/env python

import scapy.all as scp


def scan(ip):
    scp.arping(ip)

scan("10.0.2.1/24")