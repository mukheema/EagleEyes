#!/usr/bin/python

def myRange(start, stop, step):


    if stop is None:
        raise ValueError("Pass a valid integer")
    while start < stop:
        yield start
        start += step



if __name__ == '__main__':
#    myRange("hello")
    for x in myRange(1, 10.3, 2):
        print x

