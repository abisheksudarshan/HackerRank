#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful_days=[1 for t in range(i,j+1) if (t-int(str(t)[::-1]))%k==0 ]
    return sum(beautiful_days)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
