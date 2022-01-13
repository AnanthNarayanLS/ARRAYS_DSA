
# To cyclically rotate an array by one

from array import *
n = int(input("enter the length of the array : "))
arr = array('i' , [])
for i in range(n):
    temp1 = int(input("enter the values : "))
    arr.append(temp1)

print(arr)

temp = arr[0]
for i in range(1 , len(arr)):
    arr[i-1] = arr[i]
arr[-1] = temp

print(arr)
