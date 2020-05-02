#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def matches(a,b):
    if (a=="{" and b=="}") or (a=="(" and b==")") or (a=="[" and b=="]"):
        return True
    else:
        return False
def isBalanced(s):
    mystack=[]
    p="NO"
    for i in s:
        if i in ["[","{","("]:
            mystack.append(i)
        else:
            if len(mystack)==0:
                return "NO"
            else:
                b=mystack.pop()
            if matches(b,i):
                p="YES"
            else:
                return "NO"
    if len(mystack)==0:
        return p
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

