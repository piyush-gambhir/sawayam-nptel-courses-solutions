"""
Problem Statement:
Given a string S, write a function replaceV that accepts a string and replace the occurrences of 3 consecutive vowels with _ in that string. Make sure to return and print the answer string.

Input:

aaahellooo

Output:

_hell_

Explanation:

Since aaa and ooo are consecutive 3 vowels and therefor replaced by _ .
"""


def replaceV(s):
    vowels = 'aeiouAEIOU'
    res = ''
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
            if count == 3:
                res += '_'
                res = res[0: i-2] + '_'
                count = 0
                continue
        else:
            count = 0
        res += s[i]
    return res


s = input()
print(replaceV(s), end='')
