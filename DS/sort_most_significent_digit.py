#!/usr/bin/python



if __name__ == '__main__':
    arr = [ 10, 203, 5, 102, 40, 9 ]
    print "unsorted array : " + str(arr)
    s1 = sorted(arr)
    print "sorted array : " + str(s1)
    s2 = sorted(arr, key=lambda x : x % 10)
    print "sorted array with MSD : "  + str(s2)

    print "inplace sort:\n"
    print "unsorted array: " + str(arr)
    arr.sort()
    print "inplace sorted array: arr.sor() -> " + str(arr)
    arr.sort(key=lambda x : x % 10)
    print "inplace sorted array with MSD: arr.sort(key=lambda x: x % 10) -> " + str(arr)
    arr.sort(key=lambda x: x % 10, reverse=True)
    print "inplaee sorted array with MSD: arr.sort(key=lambda x: x % 10, reverse=True) -> " + str(arr)
