#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    h = 0
    l = 0
    mn = scores[0]
    mx = scores[0]

    for i in range(len(scores)):
        if mn > scores[i]:
            mn = scores[i]
            l += 1
        if mx < scores[i]:
            mx = scores[i]
            h += 1

    return h, l






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
