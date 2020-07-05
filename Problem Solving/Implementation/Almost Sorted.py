# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#checking if the table is in ascending
def checkorder(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    else:
        return True

#checking if 1 swap is enough
def checkswap(arr,i):
    arr_copy=arr.copy()
    temp=arr_copy[i]
    arr_copy[i]=arr_copy[i+1]
    arr_copy[i+1]=temp
    return checkorder(arr_copy)

#checking if reverse is an option    
def checkreverse(arr,i):
    arr_copy=arr.copy()
    temp_arr=[]
    
    #identify susbet
    for j in range(i,len(arr_copy)-1):
        if arr_copy[j+1]<arr_copy[j]:
            temp_arr.append(arr[j])
    temp_arr.append(arr_copy[j])
    
    temp_arr.sort()    
    
    new_arr=arr_copy[:i]
    
    for t in temp_arr:
        new_arr.append(t)
    
    for k in range(j+1,len(arr_copy)):
        new_arr.append(arr_copy[k])
    #print(new_arr)
    return checkorder(new_arr),j

# Complete the almostSorted function below.
def almostSorted(arr):
    swap=False
    for i in range(0,len(arr)):
        if arr[i]>arr[i+1]:
            swap=checkswap(arr,i)
            
    
    if swap==True:
        print('yes')
        print('swap {} {}'.format(i+1,i+2))
    
    if swap==False:
       #print(arr)
       reverse,j=checkreverse(arr,i) 
       #print(reverse,j)
       if reverse==True:
        print('yes')
        print('reverse {} {}'.format(i+1,j+1))
    
       else:
        print('no')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
