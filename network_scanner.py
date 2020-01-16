#!/usr/bin/env python

import scapy.all as scp


def scan(ip):
    # scp.arping(ip)
    arp_request = scp.ARP()
    arp_request.pdst = ip
    print(arp_request.summary())
    scp.ls(scp.ARP())

scan("10.0.2.1/24")