#!/usr/bin/python3

"""
method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    if type(n) is not int or n <= 1:
        return 0
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n = n / x
        x += 1
    return result
