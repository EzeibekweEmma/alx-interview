#!/usr/bin/python3

'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n):
    '''Returns min operations to get n Hs.'''

    result = 0
    index = 2
    if n < 2:
        return 0
    while (index < n + 1):
        while n % index == 0:
            result += index
            n = n / index
        index += 1
    return result
