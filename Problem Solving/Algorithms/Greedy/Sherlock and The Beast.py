#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    a, b = divmod(n,3)
    while b%5:
        b+=3
        a-=1
    print("5"*a*3+"3"*b if a>-1 else -1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
