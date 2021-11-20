
# to find a max product subarray

from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the array value : "))
    arr.append(temp)

print(f"your array is : {arr}")

def maxprosubarray(arr):
    rev_arr = arr[::-1]
    for i in range(1 , len(arr)):
        if arr[i-1] != 0:
            arr[i] *= arr[i-1]
        arr[i] *= 1

        if rev_arr[i-1] != 0:
            rev_arr[i] *= rev_arr[i-1]
        rev_arr[i] *= 1
    return max(arr + rev_arr)

print(maxprosubarray(arr))