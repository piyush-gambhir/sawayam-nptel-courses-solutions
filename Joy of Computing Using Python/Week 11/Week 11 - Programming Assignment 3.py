"""
Problem Statement:
Write a program which takes two integer a and b and prints all composite numbers between a and b.(both numbers are inclusive)

Input:
10
20

Output:
10
12
14
15
16
18
20
"""


prime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
       59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
       127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 
       191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
       257, 263, 269, 271, 277, 281, 283, 293]
Kolkata =int(input())
Mumbai=int(input())
for i in range(Kolkata ,Mumbai+1):
    if i not in prime:
        print(i)