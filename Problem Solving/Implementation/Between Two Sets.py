#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    factors_b=[]
    mul_a=[]
    #print(b,max_b)
    for i in range(1,max(b)+1):
        factors=list(filter(lambda x:x%i==0,b))
        if (len(b)==len(factors)):
            factors_b.append(i)
    for i in factors_b:
        multiples=list(filter(lambda x:i%x==0,a))
        if (len(a)==len(multiples)):
            mul_a.append(i)
    return len(mul_a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
