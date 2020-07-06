#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_=scores[0]
    min_=scores[0]
    max_count=0
    min_count=0

    for i in range(1,len(scores)):
        if max_<scores[i]:
            max_=scores[i]
            max_count+=1
        if min_>scores[i]:
            min_=scores[i]
            min_count+=1
    
    return list([max_count,min_count])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
