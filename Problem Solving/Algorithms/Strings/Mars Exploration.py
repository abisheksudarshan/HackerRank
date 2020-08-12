#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the marsExploration function below.
def marsExploration(s):
    
    count=0
    i=0

    while i<=(len(s)-3):
        temp=s[i:i+3]
        print(temp)
        if temp[0]!='S':
            count+=1
        if temp[1]!='O':
            count+=1
        if temp[2]!='S':
            count+=1
        i+=3
    
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
