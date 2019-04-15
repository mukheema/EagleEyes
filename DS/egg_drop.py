#!/usr/bin/python

INT_MAX=32767

def eggDrop(eggCount, floorCount):
    eggDropMatrix = [ [ 0 for x in xrange(floorCount + 1)] for x in xrange(eggCount + 1)]    

    print(str(eggDropMatrix))

    # we need on trial for one floor and 0 trial for 0 floors
    for i in range(1, eggCount + 1):
        eggDropMatrix[i][0] = 0
        eggDropMatrix[i][1] = 1

    #we always need j trail for one egg and j floors
    for j in range(1, floorCount + 1):
        eggDropMatrix[1][j] = 1

    # Fill the rest of entries in table using optimal substructure property
    for i in range(2, eggCount +1 ):
        for j in range(2, floorCount + 1):
            eggDropMatrix[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(eggDropMatrix[i-1][x-1], eggDropMatrix[i][j-x])
                if res < eggDropMatrix[i][j]:
                    eggDropMatrix[i][j] = res

    print (str(eggDropMatrix))

    return eggDropMatrix[eggCount][floorCount]


if __name__ == '__main__':
    n = 2
    k = 36

    print ("Minimum number of trials in worst case with " + str(n) + " eggs and " + str(k) + " floors is "  + str(eggDrop(n, k)))
