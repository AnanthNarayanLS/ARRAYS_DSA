
# SPIRAL TRAVERSAL IN A MATRIX

import numpy as np

row_end = int(input("enter the row length : "))
col_end = int(input("enter the column length : "))

matrix = []
for i in range(row_end):
    temp1 = []
    for j in range(col_end):
        temp = int(input("enter the value :"))
        temp1.append(temp)
    matrix.append(temp1)

arr = np.array(matrix)

print("the matrix is : ")
for i in range(row_end):
    for j in range(col_end):
        print(arr[i][j] , end='\t')
    print()

def spiralorder(arr , m , n):
    k , l = 0 , 0
    while (k<m and l<n):
        for i in range( l , n ):
            print(arr[k][i] , end=' ')
        k+=1

        for i in range( k , m ):
            print(arr[i][n-1] , end = ' ')
        n-=1

        #if (k<m):
        for i in range(n-1 , l-1 , -1): # l starts from 0
                print(arr[m-1][i] , end = ' ')
        m-=1

        #if (l<n):
        for i in range(m-1 , k-1 , -1):
                print(arr[i][l] ,end = ' ')
        l+=1


print(spiralorder(arr , row_end , col_end ))