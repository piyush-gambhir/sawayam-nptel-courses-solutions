"""
Problem Statement: 
Take an integer N as an input, print all the indexes of numbers in that integer from left to right.

Input:
122345

Output:
1 0 
2 1 2
3 3
4 4
5 5

Explanation:
Given integer 122345. Now printing indexes of numbers from left to right.
First number is 1 and its index is 0 therefore
1 0 

Second and third number is 2 and its index is 1,2 therefore
2 1 2

and so on...
"""

n = int(input())
idp = dict()
for i in str(n):
    idp[i] = []
    for j in range(len(str(n))):
        if i == str(n)[j]:
            idp[i] += [j]
for k in idp:
    print(k, *idp[k], "")
