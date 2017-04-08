#!/usr/bin/env python


# Given an array of all letters a-z in order. what would be the final
# state of the array after running the following algorithm.

# You need to swap (x,x+i) for all values of x and i such that x+i<27,
# So
# i = 1: You would swap first element with second element, etc.
# i.e swap(1,2), swap (2,3), swap (3,4) etc.
# i=2: you would swap first element with third element, etc.
# i.e swap(1,3),swap(2,4), swap(3,5) etc.
# continue until
# i=25 : you'd swap just the first and 26th elements.

# Starting state = abcdefghijklmnopqrstuvwxyz
# Flag = The final state of the array

s = list("abcdefghijklmnopqrstuvwxyz")

def swap(x):
    for i in range(0, len(s) - x):
        tmp = s[i]
        s[i] = s[i + x]
        s[i + x] = tmp

for i in range(0,26):
    swap(i)
    
print ''.join(s)  # zldmpnqeaiojkbgvrwshtcxfyu
