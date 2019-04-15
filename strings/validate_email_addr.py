#!/usr/bin/python

import re
import optparse


def validateEmailAddress(email=None):
    if not email:
        raise "Pass email address"
    if not isinstance(email, str):
        raise "Pass a email address string"
    emailCompilePattern = re.compile(r'(?P<EMAIL_ID>[^@]+)@(?P<COMPANY_NAME>[^@]+)\.(?P<DOMAIN>[^@|\d]+)', re.IGNORECASE)
    match_ret = emailCompilePattern.match(email)
    if match_ret:
        print "EMAIL: %s is VALID" % email
        d = match_ret.groupdict()
        print "USER ID: %s \t COMPANY: %s \t DOMAIN: %s\n" % (d['EMAIL_ID'], d['COMPANY_NAME'], d['DOMAIN'])
        return True
    else:
        print "EMAIL: %s is INVALID" % email
        return False

if __name__ == '__main__':
    user_email = str(raw_input("Enter email address: "))
    validateEmailAddress(user_email)
