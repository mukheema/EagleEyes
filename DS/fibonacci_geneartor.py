#!/usr/bin/python


def fib_recursive(num):
    if num <= 1:
#        print "rec: %d \n" %num
        return int(num)
    else:
        return fib_recursive(num - 1) + fib_recursive(num - 2)

    
def fibonacci_loop(num):
    a, b = 0, 1
    fib_list = []
    for x in xrange(num):
        print a,
        fib_list.append(a)
        a, b = b, a+b
    return fib_list


def fiboGen(num):
    a, b = 0, 1
    for x in xragen(num):
        yield a
        a, b = b, a+b

def fib_gen(num):
	a, b = 0, 1
        while True:
            if a > num:
                break
            yield a
            f  = a + b
            a = b
            b = f
               

def fibonacci_gen(maxval):
	a = 0
	b = 1
	while True:
		if a > maxval:
			break
		yield a
		future = a + b
		a = b
		b = future



if __name__ == '__main__':
    num = int(raw_input("enter a number: "))
    print ("Fibonacci series for %d is : " % num)
    for v in fibonacci_gen(num):
        print v , 

    print "\n"

    for x in fib_gen(num):
        print x,
    print "\nrecusive fibonacci series: "
    print fib_recursive(num)
