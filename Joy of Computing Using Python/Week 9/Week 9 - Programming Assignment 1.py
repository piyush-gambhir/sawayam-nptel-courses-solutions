"""
Problem Statement:
Given two string s1 and s2, write a function subStr which accepts two parameters s1 and s2 and will return True if a s2 is a substring of s1 otherwise return False. A substring is a is a contiguous sequence of characters within a string. 

Example 1:
Input:
bananamania
nana
Output:
True
Explanation:
S2 which is nana is in bananamania hence it is a substring of s1.

Example 2:
Input:
aabbcc
abc
Output:
False
Explanation:
String s1 does not contain string s2 hence the answer is false.
"""


def subStr(s1, s2):
    return (s2 in s1)


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(subStr(s1, s2), end="")
