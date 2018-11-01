#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    if len(expenditure) <= d: 
        return 0 
    numOfNotifications = 0
    dayIndex = d 
    daysPassed = 0 
    while dayIndex < len(expenditure):
        median = findMedian(expenditure[daysPassed:dayIndex])
        if expenditure[dayIndex] >= 2*median: 
            numOfNotifications +=1
        dayIndex += 1
        daysPassed +=1
    return numOfNotifications

def findMedian(arrayOfTDays):
    arrayOfTDays.sort()
    arrayLen = len(arrayOfTDays) 
    if arrayLen % 2 == 1: 
        return arrayOfTDays[arrayLen//2]
    else: 
        return (arrayOfTDays[arrayLen//2]+ arrayOfTDays[arrayLen//2 - 1]) / 2

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    # fptr.close()
