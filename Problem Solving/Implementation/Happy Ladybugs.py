#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    color_count=Counter(b)

    happy=True
    for c in color_count:
        if c!='_' and color_count[c]==1:
            happy=False
            break
    if color_count['_']==0:
        for i in range(0,len(b)-1):
            if b[i-1]!=b[i] and b[i+1]!=b[i]:
                happy=False
                break
            
    if happy:
         return 'YES' 
    else: 
        return 'NO'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
