"""
Problem Statement:

Given a matrix M write a function Transpose which accepts a matrix M and return the transpose of M.
Transpose of a matrix is a matrix in which each row is changed to a column or vice versa.

Input 
A matrix M
[[1,2,3],[4,5,6],[7,8,9]]

Output
Transpose of M
[[1,4,7],[2,5,8],[3,6,9]]

Explanation:

Matrix M was
1
1 2 3 
2
4 5 6 
3
7 8 9 


After changing all rows into columns or vice versa M will become
1
1 4 7 
2
2 5 8 
3
3 6 9
"""


def Transpose(matrix):
    transpose = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose
