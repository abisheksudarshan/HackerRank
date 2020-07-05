#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
   
    arr=[]
    for c in grid:
        arr.append([char for char in c])
    #print(arr)
   
    for i in range(1,n-1):
        for j in range(1,n-1):
            if (arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i][j+1]):
                arr[i][j] = 'X'
    return [''.join(a) for a in arr]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    #fptr.close()
