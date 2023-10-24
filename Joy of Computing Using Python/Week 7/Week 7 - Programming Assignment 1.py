"""
Problem Statement:
Given a sqaure matrix M, write a function DiagCalc that calculates the sum of left and right diagonals and prints it respectively.

Input:

A Number M 
A Matrix with M rows and M columns
[[1,2,3],[3,4,5],[6,7,8]] 

Output 
13
13

Explanation:
Sum of left diagonal is 1+4+8 = 13
Sum of right diagonal is 3+4+6 = 13
"""


def DiagCalc(M, matrix):
    leftSum = 0
    rightSum = 0
    for i in range(M):
        leftSum += matrix[i][i]
        rightSum += matrix[i][M-i-1]
    print(leftSum)
    print(rightSum, end="")


M = int(input())
matrix = []
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

DiagCalc(M, matrix)
