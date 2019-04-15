#!/usr/bin/python

import re


#ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
#ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";

def checkIPV4addr(ipv4addr=None):
    if not ipv4addr:
        raise "Pass a valid ipv4 address"
    if not isinstance(ipv4addr, str):
        raise "Pass a valid ipv4 address string"

    ipv4_pattern = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-9])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-5]|25[0-9])$', re.I)
    found = ipv4_pattern.match(ipv4addr)
    print "IPV4 address: %s is " %ipv4addr,
    if found:
        print "VALID"
        print found.group()
    else:
        print "INVALID"

if __name__ == '__main__':
    addr = str(raw_input("Enter IPV4: "))
    checkIPV4addr(addr)
