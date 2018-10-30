#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    numOfAnagrams = 0 
    i = len(s)-2 
    while i >= 0:
        ii = 0
        while ii + i < len(s)-1: 
            anagramCandidate = s[ii:ii+i+1]
            anagramCandDict = makeLettersDict(anagramCandidate)
            iterations = len(s) - len(anagramCandidate)
            iii = ii + 1 
            while iii <= iterations:
                currWordSpace = s[iii:i+iii+1]   
                currWordSpaceDict = makeLettersDict(currWordSpace)
                if currWordSpaceDict == anagramCandDict :
                    numOfAnagrams += 1
                iii += 1
            ii += 1 
        i -= 1
    return numOfAnagrams

def makeLettersDict(aString):
    _lettersDict = {} 
    for letter in aString: 
        if letter in _lettersDict: 
            _lettersDict[letter] += 1 
        else:
            _lettersDict[letter] = 1
    return _lettersDict

if __name__ == '__main__':
    # Uncomment commented lines below to get the original from the hackerrank skeleton code. 
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        # fptr.write(str(result) + '\n')

    # fptr.close()
