/*Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to

are acceptable.

For example, given the array
there are elements, two positive, two negative and one zero. Their ratios would be , and

. It should be printed as

0.400000
0.400000
0.200000

Function Description

Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):

    arr: an array of integers

*/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    po=0
    ne=0
    for a in arr:
        if(a<0):
            ne+=1
        elif(a>0):
            po+=1
    print(round(po/len(arr),6))
    print(round(ne/len(arr),6))
    print(round((len(arr)-po-ne),6)/len(arr))




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)