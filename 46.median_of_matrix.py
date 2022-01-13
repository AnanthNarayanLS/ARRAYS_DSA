
# GIVEN A ROW WISE SORTED MATRIX OF SIZE RXC WHERE R AND C ARE ALWAYS ODD, FIND THE MEDIAN OF THE MATRIX

import numpy as np

row_len = int(input("enter the row length : "))
col_len = int(input("enter the column length : "))

while (row_len * col_len)%2 == 0:
    print("PLEASE ENTER AN ODD MATRIX")
    row_len=int(input("enter the row length : "))
    col_len=int(input("enter the column length : "))

matrix = []
for i in range(row_len):
    temp1 = []
    for j in range(col_len):
        temp2 = int(input("enter the values : "))
        temp1.append(temp2)
    matrix.append(temp1)

arr = np.array(matrix)

for i in range(row_len):
    for j in range(col_len):
        print(arr[i][j] , end = '\t')
    print()

def findMatrixMedian(arr):
