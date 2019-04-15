#!/usr/bin/python

import sys
import os
import filecmp
import hashlib

def CompareByteWise(file1, file2):
	return filecmp.cmp(file1, file1)

def CompareHashWise(file1, file2):
	h1 = hashlib.md5()
	with open(file1, "r") as fd1:
		h1.update(fd1.read())
	
	h2 = hashlib.md5()
	with open(file2, "r") as fd2:
		h2.update(fd2.read())

	return h1.hexdigest() == h2.hexdigest()

if __name__ == '__main__':
	user_file1 = raw_input("Enter file1: ")
	user_file2 = raw_input("Enter file2: ")
	if not user_file1 or not user_file2:
		print("Pass both files to compare")
		sys.exit(1)

	if not os.path.isfile(user_file1) or not os.path.isfile(user_file2):
		print("Pass a valid file name")
		sys.exit(1)
	

	print("user_file1: {0} user_file2: {1}".format(user_file1, user_file2))	
	if CompareByteWise(user_file1, user_file2):
		print("ByteWise Same")
	else:
		print("ByteWise NOT Same")

	if CompareHashWise(user_file1, user_file2):
		print("HashWise Same")
	else:
		print("HashWise NOT Same")
