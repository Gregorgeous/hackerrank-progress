# Very easy, kind of a warm-up challenge rather.. (took <6 mins to write the whole code ^^ ) 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    numOfDeletion = 0
    prevIndex = 0
    for index,char in enumerate(s):
        if index is 0: 
            continue
        prevIndex = index-1
        if char == s[prevIndex]:
            numOfDeletion += 1 
    return numOfDeletion

if __name__ == '__main__':
    # UNCOMMENT BELOW FOR THE ORIGINAL HACKERRANK CODE 
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
