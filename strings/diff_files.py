#!/usr/bin/python

import os
import sys

import difflib

def difflib_diff_files(file1, file2):
	fd1 = open(file1, 'r')
	lines1 = fd1.readlines()
	fd2 = open(file2, 'r')
	lines2 = fd2.readlines()
	for line in difflib.unified_diff(lines1, lines2, fromfile=str(file1), tofile=str(file2), lineterm='\n'):
		print line

def diff_files(file1, file2):
    if not os.path.isfile(file1) or not os.path.isfile(file1):
        print("Pass a valid file names")
        return False 
    file1_lines=[]
    file2_lines=[]
    common_lines=[]
    line_count = 0
    with open(file1, 'r') as fd1, open(file2, 'r') as fd2:
        for f1Line, f2Line in zip(fd1.readlines(), fd2.readlines()):
            line_count += 1
			if f1Line == f2Line:
				common_lines.append(f1Line)
				continue
			file1_lines.append(f1Line)
			file2_lines.append(f2Line)
			
    print("-"*10)
    if len(file1_lines):
        print(file1 + ":")
        print("<".join(file1_lines))
    print("-"*10)
    if len(file2_lines):
	    print(file2 + ":")
	    print(">".join(file2_lines))
    print("-"*10)
    if len(common_lines):
        print("common contents : %d\n" % len(common_lines))
#        print(file1 + "==" + file2 + ":\n")
#        print("=".join(common_lines))

if __name__ == '__main__':
	f1 = raw_input("enter file1: ")
	f2 = raw_input("enter file2: ")
	diff_files(f1, f2)
	#difflib_diff_files(f1, f2)
