#!/usr/bin/python


import re

# sample IPV6 : fe80::89b:40ca:f1e1:c6f7%en3
# inet6 2606:b400:c11:50:c64:b9e8:97b4:899

def validateIPV6(addr=None):
    if not addr:
        raise "Pass a IPV6 addr"
    if not isinstance(addr, str):
        raise "Pass a IPV6 addr string"

    ipv6_pattern = re.compile(r'([0-9][a-f]:+){7}([0-9][a-f])+', re.I)

    found = ipv6_pattern.match(addr)
    print "IPV6: %s is " % addr , 
    if found:
        print "VALID"
    else:
        print " INVALID"


if __name__ == '__main__':
    ip = str(raw_input("Enter IPV6 addr: "))
    validateIPV6(ip)
