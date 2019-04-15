#!/usr/bin/python

import sys
import math


'''

GCD(N1, N2) = N1 * N2 / LCM(N1, N2)

LCM(N1, N2) - if N1 and N2 are either divisble of other i.e ex: 4, 16 then LCM is 16 HCF is 4
               coprime number i.e ex: 7, 8 then LCM is 7 * 8 = 56 HCF is 1


'''


def hcf_loop(x, y):
	if x < y:
		smaller = x
	else:
		smaller = y

	for i in range(1, smaller+1):
		if x % i == 0 and y % i == 0:
			gcd = i
	return gcd

def hcf_naive(x, y):
	if y == 0:
		return x
	else:
		return hcf_naive(y, x % y)

# Euclidean Algorithm
def hcf_compute(x, y):
	while(y):
		x, y = y, x%y
	return x

def lcm(x, y):
	return (x * y) / hcf_loop(x, y) 


if __name__ == '__main__':
	n1 = int(raw_input("enter a number:"))
	n2 = int(raw_input("enter a number:"))
	
	print("GCD / HCF of N1:%d and N2: %d is %d\n" %(n1, n2, hcf_loop(n1, n2)))
	print("GCD / HCF of N1:%d and N2: %d is %d\n" %(n1, n2, hcf_naive(n1, n2)))
	print("LCM of N1:%d and N2: %d is %d\n" %(n1, n2, lcm(n1, n2)))
	print("GCD of N1: %d and N2: %d is %d\n" %(n1, n2, hcf_compute(n1, n2)))

	#print("GCD / HCD math N1:%d and N2:%d is %d\n" %(n1, n2, math.gcd(n1, n2)))
	#print("LCM math N1:%d and N2:%d is %d\n" %(n1, n2, math.lcm(n1, n2)))
