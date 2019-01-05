#!/bin/python3

import math
import os
import random
import re
import sys

def icecreamParlor(m, arr):
    numsEncountered = dict()
    price1Index, price2Index = None, None 
    for index,price in enumerate(arr):
        correspondingNum = m - price
        if correspondingNum in numsEncountered:
            # We need to return the "human-read index :>" (1-based, not 0-based) thus both priceIndices are "+1"
            price1Index = index + 1
            price2Index = numsEncountered[correspondingNum] + 1
            break
        numsEncountered[price] = index
    # This is theoretically not necessary as the challenge description restricts no-pairs .. but .. at least we can show-off knowing the "for-else" python syntax :D 
    else: 
        print("No pair found!")

    if price1Index > price2Index:
        return [price2Index, price1Index]
    else:
        return [price1Index, price2Index]

if __name__ == '__main__':
    # UNCOMMENT BELOW FOR THE ORIGINAL HACKERRANK CODE 
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
