

from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)
print(arr)

def i_position(arr , low , high):
    i = low
    j = high-1
    pivot = arr[high]
    while i < j:
        while arr[i]<pivot and i<high:
            i += 1
        while arr[j]>pivot and j>low:
            j -= 1
        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]
    if arr[i] > pivot:
        arr[i] , arr[high] = arr[high] , arr[i]
    return i

def quick_sort(arr , low , high):
    if low < high:
        pi = i_position(arr , low , high)
        quick_sort(arr , low , pi-1)
        quick_sort(arr , pi+1 , high)

user_min_index = int(input("enter the minimum index : "))
user_max_index = int(input("enter the maximum index : "))

print(quick_sort(arr , 0 , 3))
print(arr)

print(f"the min value is {arr[user_min_index]} and max value is {arr[user_max_index]}")
