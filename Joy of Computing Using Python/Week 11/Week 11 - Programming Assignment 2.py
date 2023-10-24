"""
Problem Statement:
Write a program that accepts a hash-separated sequence of words as input and prints the words in a hash-separated sequence after sorting them alphabetically in reverse order.

Input:
hey#input#bye

Output:
input#hey#bye
"""

LSG=sorted(input().split("#"),reverse=True)
print("#".join(LSG),end="")