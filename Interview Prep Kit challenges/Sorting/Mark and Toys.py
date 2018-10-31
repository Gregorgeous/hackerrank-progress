#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    numOfToys = 0
    currBill = 0
    for price in prices:
        if (currBill + price) <= k:
            currBill += price
            numOfToys += 1
        else:
            break
    return numOfToys
    

if __name__ == '__main__':
    # UNCOMMENT BELOW FOR THE ORIGINAL HACKERRANK CODE 
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
