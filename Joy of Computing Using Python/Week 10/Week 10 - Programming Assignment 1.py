"""
Problem Statement:
Given a list L write a program to make a new list and match the numbers inside list L to its respective index in the new list. Put 0 at remaining indexes. Also print the elements of the new list in the single line. (See explanation for more clarity.)

Input:
[1,5,6]

Output:
0 1 0 0 0 5 6

Explanation: 
List L contains 1,5,9 so at 1,5,9, index of new list the respective values are put and rest are initialized as zero.
"""

L = [int(i) for i in input().split()]
ans = [0]*(max(L)+1)
for i in range(len(ans)):
    if i in L:
        ans[i] = i
print(*ans, end="")
