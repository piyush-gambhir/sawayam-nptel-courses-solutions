"""
Problem Statement:
Given a list of strings, write a program to write sort the list of strings on the basis of last character of each string.

Input:
L = ['ram', 'shyam', 'lakshami']

Output:
['lakshami', 'ram', 'shyam']
"""

LSG = input().split()
MI = []
for i in LSG:
    MI.append("".join(list(i)[::-1]))
ans = []
for i in sorted(MI):
    ans.append("".join(list(i)[::-1]))
print(ans, end="")
