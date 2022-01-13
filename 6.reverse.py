
from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the array value : "))
    arr.append(temp)

print(f"your array is : {arr}")

print("------------------------------------")

print(arr[::-1])

print("------------------------------------")

def reversearray(arr , start = 0 , end = len(arr)-1):
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
    print(arr)

print(reversearray(arr))