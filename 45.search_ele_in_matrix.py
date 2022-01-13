
# TO SEARCH AN ELEMENT IN A MATRIX

import numpy as np

row_len = int(input("enter the length of the row : "))
col_len = int(input("enter the length of the column : "))

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
        print(arr[i][j] , end= '\t')
    print()

search_ele = int(input("enter the element to search : "))

for i in range(row_len):
    for j in range(col_len):
        if arr[i][j] == search_ele:
            print(f"element is present at : {i,j}")
