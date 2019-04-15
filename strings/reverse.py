#!/usr/bin/python

def rev_recursive(word, start, end):
    if start < end -1:
        word[start], word[end-1] = word[end-1], word[start]
        print word
        rev_recursive(word, start+1, end-1)


if __name__ == '__main__':
    s1 = "hello world"
    print("start - s1: %s" % s1)
    s2 = list(s1)
    rev_recursive(s2, 0, len(s2))
#print("rev -s1 %s ", [ ''.join(c) for c in  s2 ])
    print "rev s1 : %s is %s\n" % (s1, "".join(s2))
