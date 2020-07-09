#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    
    counts = Counter(s1)
    counts.subtract(s2)
    return (sum(abs(x) for x in counts.values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
Making Anagrams
