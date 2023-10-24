"""
Problem Statement:

Given a matrix M write a function snake that accepts a matrix M and returns a list which contain elements in snake pattern of matrix M. (See explanation to know what is a snake pattern)

Input
A matrix M
91 59 21 63 
81 39 56 8 
28 43 61 58 
51 82 45 57

Output
[91, 59, 21, 63, 8, 56, 39, 81, 28, 43, 61, 58, 51, 82, 45, 57]

Explanation:

For row 1 elements are inserted from left to right
For row 2 elements are inserted from right to left
For row 3 elements are inserted form left to right 
and so on
"""


def Snake(matrix):
    snake = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix[0])):
                snake.append(matrix[i][j])
        else:
            for j in range(len(matrix[0])-1, -1, -1):
                snake.append(matrix[i][j])
    return snake
