#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a = Counter(a)
    print(a)
    maxi = 0
    for k in sorted(a):
        m = a[k]+a.get(k+1,0)
        print(m)
        if maxi<m:
            maxi=m
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
