'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example,
. Our minimum sum is and our maximum sum is

. We would print

16 24

Function Description

Complete the miniMaxSum function in the editor below. It should print two space-separated integers on one line: the minimum sum and the maximum sum of
of

elements.

miniMaxSum has the following parameter(s):

    arr: an array of 

    integers

Input Format

A single line of five space-separated integers.

Constraints

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min=0
    max=0
    sum=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i!=j:
                sum+=arr[j]
        if(min==0 or min>sum):
            min=sum
        if(max==0 or max<sum):
            max=sum
        sum=0
    print(min,max)    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
