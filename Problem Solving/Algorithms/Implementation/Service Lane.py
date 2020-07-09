#!/bin/python3Chocolate Feast

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases, width):
    veh=[]
    for c in cases:
        start=c[0]
        end=c[1]
        veh.append(min(width[start:end+1]))
    return veh

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
