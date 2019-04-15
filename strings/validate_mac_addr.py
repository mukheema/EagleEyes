#!/usr/bin/python

import re

def checkMacAddr(addr=None):
    if not addr:
        raise "Pass a valid mac address to check"
    pat = re.compile(r'^((\d|[a-f]){1,2}:){5}(\d|[a-f]){1,2}$', re.I)
    if pat.match(addr):
        if len(addr.split(':')) == 6:
            return True
    return False


if __name__ == '__main__':
    user_addr = str(raw_input("Enter mac address to check: "))
    print "Mac Addr : %s " % user_addr ,
    if checkMacAddr(user_addr):
        print ": Valid"
    else:
        print ": In-Valid"
