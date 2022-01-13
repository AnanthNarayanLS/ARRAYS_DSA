

from array import *

n = int(input("enter the number of elements :"))

arr = array('i',[])
for i in range(n):
    temp = int(input("enter the elements : "))
    arr.append(temp)

print(arr)

def subarray(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            for k in range(arr[i] , arr[j]):
                print(arr[k])

print(subarray(arr))