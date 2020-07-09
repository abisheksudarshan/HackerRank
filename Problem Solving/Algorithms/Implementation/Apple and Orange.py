#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    new_apples= [num+a for num in apples]
    new_oranges= [num+b for num in oranges]
    apples_nearby= list(filter(lambda num:num>=s and num<=t,new_apples ))
    oranges_nearby= list(filter(lambda num:num>=s and num<=t,new_oranges ))
    print(len(apples_nearby))
    print(len(oranges_nearby))


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
Apple and Orange
