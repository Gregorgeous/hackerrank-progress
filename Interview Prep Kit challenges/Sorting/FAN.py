#!/bin/python3
import math
import os
import random
import re
import sys

import heapq 


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    if len(expenditure) <= d: 
        return 0 
    numOfNotifications = 0
    dayIndex = d
    halfOfD1 = None
    halfOfD2 = None
    if d % 2 == 1:
        halfOfD1 = d//2 
    else:
        halfOfD1 = d//2
        halfOfD2 = halfOfD1-1
    trailDaysArray, countArray = countSort(expenditure[:d])
    while dayIndex < len(expenditure):
        median = findMedian(trailDaysArray, halfOfD1, halfOfD2)
        if expenditure[dayIndex] >= 2*median: 
            numOfNotifications +=1
        trailDaysArray, countArray = updateCountSort(trailDaysArray,trailDaysArray[-1],countArray,expenditure[dayIndex] )
        dayIndex += 1
    return numOfNotifications

def findMedian(arrayOfTDays,halfOfD1, halfOfD2):
    arrayLen = len(arrayOfTDays) 
    if halfOfD2:
        return arrayOfTDays[halfOfD1]
    else: 
        return (arrayOfTDays[halfOfD1]+ arrayOfTDays[halfOfD2]) / 2

def updateCountSort(trailDaysArray, maxNum, countArray, newNum):
    if newNum > maxNum:
        for i in range(newNum-maxNum):
            countArray.append(0)
    countArray[newNum] += 1 
    oldNum = trailDaysArray[0]
    countArray[oldNum] -= 1
    # trailDaysArray = trailDaysArray[1:]
    return countSort(None, maxNum, countArray) 

def countSort(expenditure, maxNum = None, countArray = None):
    if maxNum == None: 
        maxNum = max(expenditure)
    if countArray == None:
        print("test1")
        countArray = [0 for i in range(maxNum+1)] 
        for num in expenditure: 
            countArray[num] += 1
        print("test2")

    sortedList = []

    for item, count in enumerate(countArray):

        # For the number of times the item occurs
        for _ in range(count):

            # Add it to the sorted list
            sortedList.append(item)
    
    return sortedList, countArray


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
