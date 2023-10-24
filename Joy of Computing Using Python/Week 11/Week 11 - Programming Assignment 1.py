"""
Problem Statement:
Take 3 sides of a triangle as an input and find whether that triangle is a right angled triangle or not. Print 'YES' if a triangle is right angled triangle or 'NO' if it's not.

Input:
3
4
5

Output:
YES
"""

a=int(input())
b=int(input())
c=int(input())
LG=[a,b,c]
h=max(LG)
LG.remove(h)
if h**2==LG[0]**2+LG[1]**2:
  print("YES",end="")
else:
  print("NO",end="")