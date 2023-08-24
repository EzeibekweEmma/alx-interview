#!/usr/bin/python3
"""Module for validUtf8"""


def validUTF8(data):
    """Check if a list of integers is a valid utf-8 set"""
    nbytes = 0

    byte1 = 1 << 7
    byte2 = 1 << 6

    for number in data:
        b = 1 << 7
        if nbytes == 0:
            while b & number:
                nbytes += 1
                b = b >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (number & byte1 and not (number & byte2)):
                return False
        nbytes -= 1
    return nbytes == 0
