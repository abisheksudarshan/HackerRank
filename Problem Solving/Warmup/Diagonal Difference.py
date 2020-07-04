'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix

is shown below:

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal =
. The right to left diagonal = . Their absolute difference is

.

Function description

Complete the

function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

    arr: an array of integers .

Input Format

The first line contains a single integer,
, the number of rows and columns in the matrix .
Each of the next lines describes a row, , and consists of space-separated integers

.

Constraints

Output Format

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    l=0
    r=0
    for i in range (0,len(arr)):
        for j in range (0,len(arr)):
            if(i==j):
                l=l+arr[i][j]
                #print(l)
            if(i+j)==(len(arr)-1):
                r=r+arr[i][j]
    return (abs(l-r))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
