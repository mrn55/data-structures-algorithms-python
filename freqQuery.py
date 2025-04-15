#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQueryOld(queries):
    freq = {}
    output = []
    for q in queries:
        # q is the type of operation (1=insert, 2=delete, 3=check for freq exaclty n amount)
        match q[0]:
            case 1:
                freq[q[1]] = freq.get(q[1], 0) + 1
            case 2:
                if q[1] in freq:
                    freq[q[1]] -= 1
            case 3:
                output.append(1 if q[1] in freq.values() else 0)
        # print(arr)
    return output

def freqQuery(queries):
    freq = {}
    freq_count = {}
    output = []

    for op, val in queries:
        if op == 1:
            old_freq = freq.get(val, 0)
            new_freq = old_freq + 1
            freq[val] = new_freq

            freq_count[old_freq] = freq_count.get(old_freq, 0) - 1 if old_freq in freq_count else 0
            freq_count[new_freq] = freq_count.get(new_freq, 0) + 1

        elif op == 2:
            old_freq = freq.get(val, 0)
            if old_freq > 0:
                new_freq = old_freq - 1
                freq[val] = new_freq

            freq_count[old_freq] = freq_count.get(old_freq, 0) - 1
            freq_count[new_freq] = freq_count.get(new_freq, 0) + 1

        elif op == 3:
            output.append(1 if freq_count.get(val, 0) > 0 else 0)

    return output

def main():
    queries = [(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]
    ans = freqQuery(queries)
    print(ans)

    queries = [
    [1, 5],
    [1, 6],
    [3, 2],
    [1, 10],
    [1, 10],
    [1, 6],
    [2, 5],
    [3, 2]
    ]
    print(freqQuery(queries))  # Output: [0, 1]

if __name__ == '__main__':
    main()