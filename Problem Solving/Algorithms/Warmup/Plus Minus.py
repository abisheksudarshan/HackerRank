#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    po=0
    ne=0
    for a in arr:
        if(a<0):
            ne+=1
        elif(a>0):
            po+=1
    print(round(po/len(arr),6))
    print(round(ne/len(arr),6))
    print(round((len(arr)-po-ne),6)/len(arr))




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
