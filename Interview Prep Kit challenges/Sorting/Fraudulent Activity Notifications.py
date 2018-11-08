#!/bin/python3
import math
import os
import random
import re
import sys

def activityNotifications(expenditure, d):
    if len(expenditure) <= d: 
        return 0 
    numOfNotifications = 0
    dayIndex = d
    halfIndex1 = None
    halfIndex2 = None
    if d % 2 == 1:
        halfIndex1 = d//2
    else:
        halfIndex1 = d//2 - 1
        halfIndex2 = halfIndex1+1
    countArray, maxNum =countSort(expenditure[:d])
    for dayIndex in range(d, len(expenditure)):
        median = findMedian(countArray, halfIndex1, halfIndex2)
        if expenditure[dayIndex] >= 2*median: 
            numOfNotifications +=1
        countArray,maxNum = updateCountArray(countArray,expenditure[dayIndex], expenditure[dayIndex-d], maxNum)
    return numOfNotifications

def countSort(expenditure):
    # NOTE: Although the idea the idea of using "max" compared to hard-coded 200 range (risking a bit of space redundancy) BUT the space is 0 < i <= 200 wheareas 'd' can be really huge, thus making 'max(expenditure)' really long. 
    # maxNum = max(expenditure)
    maxNum = 200
    countArray = [0] * (maxNum + 1) 
    for num in expenditure: 
        countArray[num] += 1
    return countArray, maxNum

def findMedian(countArray,halfIndex1, halfIndex2):
    counter = 0
    half1AlreadyFound = False
    for index,num in enumerate(countArray):
        counter += num
        if halfIndex2 is None :
            if counter > halfIndex1:
                first = index
                break 
        else: 
            if counter > halfIndex1 and not half1AlreadyFound:
                first = index
                half1AlreadyFound = True
            if counter > halfIndex2 :
                second = index
                break
    if halfIndex2 is None:
        return first
    else: 
        return (first+second)/2

def updateCountArray(countArray,newNum, oldNum, maxNum):
    # NOTE: see the comment in def countSort.
    # if newNum > maxNum:
    #     for _ in range(newNum-maxNum):
    #         countArray.append(0)
    countArray[newNum] += 1 
    countArray[oldNum] -= 1
    return countArray, maxNum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))


    result = activityNotifications(expenditure, d)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
