#!/bin/python3


import math
import os
import random
import re

import sys


def candies(n, ratings):
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

def main():

    arr= [2,4,2,6,1,7,8,9,2,1]
    arr= [1,2,2]

    n = len(arr)
    print(candies(n, arr))


if __name__ == '__main__':
    main()





# child:  0 1 2 3 4 5 6 7 8 9
# rating: 2 4 2 6 1 7 8 9 2 1

# candy:  1 2 1 2 1 2 3 4 2 1    

