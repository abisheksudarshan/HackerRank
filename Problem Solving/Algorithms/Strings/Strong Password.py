#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    numcount=0
    lcasecount=0
    ucasecount=0
    specialcount=0
    slen=len(password)

    for char in password:
        if char in numbers:
            numcount=1
        if char in lower_case:
            lcasecount=1
        if char in upper_case:
            ucasecount=1
        if char in special_characters:
            specialcount=1
        
    char_needed=4-(numcount+lcasecount+ucasecount+specialcount)
    
    if (slen>=6) or (slen+char_needed>=6):
        return char_needed
    else:
        return 6-(slen)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
