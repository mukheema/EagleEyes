#!/usr/bin/python

import sys

def isPrimeNumber(num):
    for i in xrange(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    userNum = raw_input("Enter a number: ")
    if not userNum.isdigit():
        print("Pass a valid number")
        sys.exit(1)
    # userNum = int(userNum)
    if isPrimeNumber(int(userNum)):
        print("%s is a Prime Number" % userNum)
    else:
        print("%s is Non Prime Number" % userNum)
    sys.exit(0)
