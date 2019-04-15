#!/usr/bin/python


def encodeMsg(msg=None):
    if msg:
        return ''.join([ chr(ord(x) + 40) for x in msg ])

def decodeMsg(msg=None):
    if msg:
        return ''.join([ chr(ord(x) - 40) for x in msg ])

if __name__ == '__main__':
    s1 = raw_input("enter a string to encrypt: ")
    print("User enter str: " + s1)
    s2 = encodeMsg(s1)
    print("Ecrypted str: %s " % s2)
    print("Decrypted str: %s " % decodeMsg(s2))
