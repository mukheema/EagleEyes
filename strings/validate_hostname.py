#!/usr/bin/python
import re   

def validateHostName(name=None):
    if not name:
        raise "Pass a hostname"
    if not isinstance(name, str):
        raise "Pass a hostname string"
    hostname_pattern = re.compile(r'^(\w[^\W])*\.(\w)*\.(\w)*', re.I)
    found = hostname_pattern.match(name)
    if found:
        print "Host: %s is VALID" % name
    else:
        print "Host: %s is INVALID" % name


if __name__ == '__main__':
   validateHostName("mukheem-mac") 
