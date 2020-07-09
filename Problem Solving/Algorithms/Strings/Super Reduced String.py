#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    stack=[]
    for char in s:
        if stack!=[] and char==stack[-1]:
            stack.pop()
        else:
            stack.append(char)
        
    if stack==[]:
        return 'Empty String'
    else:
        return ''.join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
