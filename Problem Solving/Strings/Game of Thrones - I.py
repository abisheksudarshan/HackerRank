#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    add = 0
    for x in Counter(s).values():
        add+=x%2
    return "NO" if add>1 else "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
