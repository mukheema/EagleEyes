#!/usr/bin/python

import os
from pprint import pprint


class GetDuplicateFiles:

    def __init__(self, path_name=None):
        self._path_name = path_name
        self._files = []
        self._duplicate_files = []

    def validate_path(self):
        if os.path.isdir(self._path_name):
            return True
        print("%s is not a valid directory" %self._path_name)
        return False

    def listAllFiles(self):
        for root, sub_dirs, files in os.walk(self._path_name):
            print "root - " + root + "sub_dirs: " + str(sub_dirs) + "files: " + str(files)
            self._files.extend([os.path.join(root, leaf) for leaf in files])
            pprint("inner files: %s" %self._files)
        pprint("files : %s" %self._files)

    def checkDuplicateFiles(self):
        if not self._files:
            self.listAllFiles()
        for f in self._files:
            check_file = os.path.basename(f)
            for x in self._files:
                if check_file == os.path.basename(x):
                    self._duplicate_files.append(x)
        self._duplicate_files = list(set(self._duplicate_files))

class CheckDuplicateFiles(object):
    def __init__(self, user_path):
        self._path = user_path
        self._allFiles = None
        self._duplicateFiles = None

    def listAllFiles(self):
        for f in os.listdir(self._path):
            if os.path.isdir(f):
                pass
                


if __name__ == '__main__':
	user_path = raw_input("enter a path")
	dup_files = GetDuplicateFiles(user_path)
	dup_files.validate_path()
	dup_files.checkDuplicateFiles()
	print("Duplicate files:")
	for x in dup_files._duplicate_files:
		print("Dup: %s\n" % x)
