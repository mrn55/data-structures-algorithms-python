#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSumOld(arr):
    n = len(arr) # do this since we need it more later
    if n == 0: # no use continuing if there are no or just 1 element
        return 0
    elif n == 1:
        return arr[0]

    dp = [0] * n # use a 0 filled array the same length as arr to track sum
    dp[0] = arr[0] # only possible sum at i=0
    dp[1] = max(arr[0], arr[1]) # take the max between i=0 and i=1 since you cant have both

    for i in range(2, n):
        # At each i, we have 3 options:
        # 1. dp[i-1] → we skip arr[i]
        # 2. arr[i] + dp[i-2] → take arr[i], skip previous
        # 3. arr[i] → start fresh from current, in case all prior sums are negative
        dp[i] = max(dp[i-1], arr[i]+dp[i-2], arr[i])

    # the max will be on the end of dp, accessed at -1 index (python)
    return dp[-1]

def maxSubsetSum(arr):
    n = len(arr) # do this since we need it more later
    if n == 0: # no use continuing if there are no or just 1 element
        return 0
    elif n == 1:
        return arr[0]

    prev2 = arr[0]
    prev1 = max(arr[0], arr[1])

    for i in range(2, n):
        current = max(prev1, arr[i] + prev2, arr[i])
        prev2 = prev1
        prev1 = current

    return prev1
