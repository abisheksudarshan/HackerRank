#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    c=Counter(arr)
    maxval=max(c.values())
    mink=-1
    #print(maxval,mink)
    for k,v in c.items():
        if maxval==v and (mink>k or mink==-1):
            mink=k
    return mink

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
