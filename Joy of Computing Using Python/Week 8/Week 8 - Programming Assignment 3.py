"""
Problem Statement:

Write a program that take list L as an input and shifts all zeroes in list L towards the right by maintaining the order of the list. Also print the new list.

Input:

[0,1,0,3,12]

Output:

[1,3,12,0,0]

Explanation:

There are two zeroes in the list which are shifted to the right and the order of the list is also maintained. (1,3,12 are in order as in the old list.)
"""


def shiftZeros(L):

    L = [x for x in L if x != 0] + [0] * L.count(0)
    return L


L =list(map(int, input().split()))

print(shiftZeros(L), end='')
