
# NOT EXECUTING TRACE AGAIN


# TO FIND A ROW HAVING MAXIMUM NUMBER OF 1's

import numpy as np

row_len = int(input("enter the number of rows : "))
col_len = int(input("enter the number of col : "))

matrix = []

for i in range(row_len):
    temp = []
    for j in range(col_len):
        val = int(input("enter the value : "))
        temp.append(val)
    matrix.append(temp)

arr = np.array(matrix)

for i in range(row_len):
    for j in range(col_len):
        print(arr[i][j] , end= '\t')
    print()

 # RETURNS ME THE LIST OF MAX 1'S IN A ROW
max1srow = []
for i in range(len(arr)):
    temp=0
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            temp+=1
    max1srow.append(temp)

 # RETURNS ME THE LIST OF MAX 1'S IN A col
max1scol = []
for i in range(len(arr[0])):                    # len(col) = len(arr[0])
    temp=0
    for j in range(len(arr)):                   # len(row) = len(arr)
        if arr[i][j] == 1:
            temp+=1
    max1scol.append(temp)

for i in range(len(max1srow)):
    for j in range(i+1 , len(max1srow)):
        for k in range(j+1 , len(max1srow)):
            if (max1srow[i] == max1srow[j] == max1srow[k]) and (j-i)==1 and (k-j)==1:
                # print 3 rows having same 1s
                print(f"the rows having max ones are {i},{j},{k}")
            elif (max1srow[i] == max1srow[j]) and (j-i)==1:
                # print 2 rows having same 1s
                print(f"the rows having the max 1s are {i},{j}")
            else:
                # print the max row
                print(f"the row having max 1s is {max1srow.index(max(max1srow))}")
for i in range(len(max1scol)):
    for j in range(i+1 , len(max1scol)):
        for k in range(j+1 , len(max1scol)):
            if (max1scol[i] == max1scol[j] == max1scol[k]) and (j-i)==1 and (k-j)==1:
                # print 3 col having same 1s
                print(f"the col having max ones are {i},{j},{k}")
            elif (max1scol[i] == max1scol[j]) and (j-i)==1:
                # print 2 col having same 1s
                print(f"the col having the max 1s are {i},{j}")
            else:
                # print the max col
                print(f"the col having max 1s is {max1scol.index(max(max1scol))}")








