#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    coloursDict = {}
    for socksColour in ar:
        if socksColour in coloursDict:
            coloursDict[socksColour] += 1
        else:
             coloursDict[socksColour] = 1
    numOfPairs = 0 
    for _, colour in coloursDict.items():
        numOfPairs += colour // 2
    return numOfPairs

if __name__ == '__main__':
    # UNCOMMENT BELOW FOR THE ORIGINAL HACKERRANK PROGRAM STRUCTURE 
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # ar = list(map(int, input().rstrip().split()))

    # COMMENT BOTH VARS BELOW FOR THE ORIGINAL HACKERRANK PROGRAM STRUCTURE
    n = 9
    ar = [10,20,20,10,10,30,50,10,20]

    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()
