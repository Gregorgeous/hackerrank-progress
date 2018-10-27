#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    bribes_dict= {}
    bribes = 0
    for index in range(0,len(q)-1):
        if q[index] > q[index+1] :
            i = index + 1
            while  q[i-1] > q[i]and i > 0:
                q[i], q[i-1] =q[i-1],q[i]
                bribes += 1
                if q[i] in bribes_dict:
                    bribes_dict[q[i]] += 1
                else:
                    bribes_dict[q[i]] = 1
                if bribes_dict[q[i]] > 2:
                    print ("Too chaotic")
                    return 
                i -= 1
    print(bribes)
    return bribes    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
