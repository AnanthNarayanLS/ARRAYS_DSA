
# to rotate the matrix 90 degree clockwise

import numpy as np

arr_len = int(input("enter the matrix length : "))

matrix = []
for i in range(arr_len):
    temp = []
    for j in range(arr_len):
        val = int(input("enter the values : "))
        temp.append(val)
    matrix.append(temp)

arr = np.array(matrix)
for i in range(arr_len):
    for j in range(arr_len):
        print(arr[i][j] , end = '\t')
    print()

def rotate90Clockwise(arr , n):
    for j in range(n):
        for i in range(n-1, -1, -1):
            print(arr[i][j], end="\t")
        print()

print(rotate90Clockwise(arr , arr_len))