#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    currentHeightLevel = 0
    inValley = False
    numOfValleys = 0
    for i in range(len(s)):
        if s[i] == "D":
            if currentHeightLevel == 0 :
                inValley = True
            currentHeightLevel -= 1
        else:
            currentHeightLevel += 1
            if currentHeightLevel == 0 and inValley==True:
                numOfValleys += 1
                inValley = False
    return numOfValleys

if __name__ == '__main__':
    # UNCOMMENT BELOW FOR THE ORIGINAL HACKERRANK PROGRAM STRUCTURE 
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # s = input()

    # COMMENT BOTH VARS BELOW FOR THE ORIGINAL HACKERRANK PROGRAM STRUCTURE
    n = 8
    s = ['U','D','D','D','U','U','D','U']

    result = countingValleys(n, s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
