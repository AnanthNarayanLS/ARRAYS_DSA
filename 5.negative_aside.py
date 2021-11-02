
from array import *

num = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(num):
    temp = int(input("enter the values : "))
    arr.append(temp)
print(arr)

index_n  = 0
for i in range(len(arr)):
    if arr[i] == arr[-i]:
        arr[index_n] , arr[i] = arr[i] , arr[index_n]
        index_n += 1

print(arr)