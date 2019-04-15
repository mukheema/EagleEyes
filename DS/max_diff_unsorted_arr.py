#!/usr/bin/python


def max_diff(array=None):
    if not array:
        raise "Pass a valid array of integers"
    arrayLen = len(array)
    # single element in a array no max_diff
    if arrayLen == 1:
        return 0
    maxDiffLen = array[0]
    for i in range(0, arrayLen):
        for j in range(i, arrayLen):
            if array[j - 1] > array[j]:
                maxDiffLen = array[j]

    return maxDiffLen

# Driver code start here
if __name__ == '__main__':
    arr = [ 2, 5, 10, 8, 3, 4]

    print "max diff betweeen largest and samllest number in unsorted array is: " + str(max_diff(arr))
