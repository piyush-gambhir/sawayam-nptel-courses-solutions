"""
Problem Statement:
Ram shifted to a new place recently. There are multiple schools near his locality. Given the co-ordinates of Ram P(X,Y) and schools near his locality in a nested list, find the closest school. Print multiple coordinates in respective order if there exists multiple schools closest to him. Write a function closestSchool that accepts (X ,Y , L) where X and Y are co-ordinates of Ram's house and L contains co-ordinates of different school.

Distance Formula(To calculate distance between two co-ordinates): √((X2 - X1)² + (Y2 - Y1)²)

where (x1,y1) is the co-ordinate of point 1 and (x2, y2) is the co-ordinate of point 2.

Input:
X, Y (Ram's house co-ordinates)
N (No of schools)
X1 Y1
X2 Y2
.
.
.

X6 Y6

Output:
Closest pont/points to X, Y
"""


def closestSchool(x, y, L):
    min = 999466
    distance = []
    for a in L:
        dis = ((x-a[0])**2+(y-a[1])**2)**0.5
        distance.append(dis)
        if dis < min:
            min = dis
    for i in range(len(distance)):
        if distance[i] == min:
            print(L[i])
