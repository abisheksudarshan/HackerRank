#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    counter=0
    level=0
    for i in range(n):
        if s[i]=='U':
            level+=1
        if s[i]=='D':
            level-=1
        
        if level==0 and s[i]=='U':
            counter+=1
        

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
