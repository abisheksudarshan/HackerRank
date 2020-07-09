#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    kap=[]
    for i in range(p,q+1):
        square=i**2
        i_str=str(i)
        square_str=str(square)
        r=square_str[len(square_str)-len(i_str):]
        l=square_str[:len(square_str)-len(i_str)]
        
        #print (i,l,r)
        if len(l)==0:
            if i==int(r):
                kap.append(str(i))
        if len(l)>0:
            if i==(int(l)+int(r)):
                kap.append(str(i))
    if kap==[]:
        print('INVALID RANGE')
    else:
        print(' '.join(kap))    

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
