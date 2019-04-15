#!/usr/bin/python


def longestPalindormNumber(num1, num2):
    longestNum = 0
    if num1 <= 0 or num2 <= 0:
        print "longest Palindorme for negavite number not done"
    for d in xrange(1, num1*num2):
        if str(d) == str(d)[::-1]:
            # print "series num: %d\n" %d
            longestNum = d
    #    else:
            # print("%d is not a palindorme" %d)
    print "Longest Palindorme is %d\n" %longestNum


if __name__ == '__main__':
    longestPalindormNumber(int(raw_input("enter num1:")), int(raw_input("enter num2:")))

    
