#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the pangrams function below.
def pangrams(s):
    s = set(s.lower())
    s.discard(" ")
    s.discard("\n")
    s.discard(".")
    #print(set(string.ascii_lowercase))
    #print(s)
    #print(s==set(string.ascii_lowercase))
    return "pangram" if s==set(string.ascii_lowercase)  else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
