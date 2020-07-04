#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min=0
    max=0
    sum=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i!=j:
                sum+=arr[j]
        if(min==0 or min>sum):
            min=sum
        if(max==0 or max<sum):
            max=sum
        sum=0
    print(min,max)    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
