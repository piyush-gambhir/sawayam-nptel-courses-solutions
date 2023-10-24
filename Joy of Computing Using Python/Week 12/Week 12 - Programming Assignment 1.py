"""
Problem Statement:
Write a program to an integer as an input and reverse that integer.

Input:
A single integer.

Output:
Reverse number of that integer.

Example:
Input:
54321

Output:
12345
"""

n = int(input())
print(int("".join(list(str(n))[::-1])), end="")
