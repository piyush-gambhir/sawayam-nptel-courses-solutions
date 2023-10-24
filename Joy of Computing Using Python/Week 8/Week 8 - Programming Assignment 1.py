"""
Problem Statement:
Given a Tuple T, create a function squareT that accepts one argument and returns a tuple containing similar elements given in tuple T and its sqaures in sequence.

Input:

(1,2,3)

Output :

(1,2,3,1,4,9)

Explanation:

Tuple T contains (1,2,3) the output tuple contains the original elements of T that is 1,2,3 and its sqaures 1,4,9 in sequence.
"""


def squareT(T):
    for i in range(len(T)):
        T += (T[i] * T[i],)
    return T


