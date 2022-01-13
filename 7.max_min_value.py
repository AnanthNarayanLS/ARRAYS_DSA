

from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the array value : "))
    arr.append(temp)

print(f"your array is : {arr}")

def index_i(arr , low , high):
    i = low
    j = high-1
    pivot = arr[high]
    while i < j:
        while i < high and arr[i] < pivot:
            i+=1
        while j > low and arr[j] > pivot:
            j-=1
        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]
    if arr[i] > pivot:
        arr[i] , arr[high] = arr[high] , arr[i]
    return i

def quicksort(arr , low, high):
    if low < high:
        pi = index_i(arr , low , high)
        quicksort(arr , low , pi-1)
        quicksort(arr , pi+1 , high)


print(quicksort(arr , low = 0 , high = len(arr)-1))
print(f"the sorted arrray is : {arr}")
print(f"the min is : {arr[0]}")
print(f"the max is : {arr[-1]}")