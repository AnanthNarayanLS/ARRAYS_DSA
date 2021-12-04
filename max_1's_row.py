
# TO FIND A ROW HAVING MAXIMUM NUMBER OF 1's

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

ones_count = []
for i in range(row_len):
    temp=0
    for j in range(col_len):
        if arr[i][j] == 1:
            temp+=1
    ones_count.append(temp)

print(ones_count)
print(f"the row having the maximum ones is {ones_count.index(max(ones_count))} and the count is {max(ones_count)}")

