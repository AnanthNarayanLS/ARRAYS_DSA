
# to rearrange the given array in alternating positive and negative items with 0(1) T.Complex.

from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the array value : "))
    arr.append(temp)

print(f"your array is : {arr}")

# quick sort....
def partition(customlist , low , high):
     i = low
     j = high-1
     pivot = customlist[high]
     while i<j:
         while i< high and customlist[i]<pivot:
             i+=1
         while j> low and customlist[j]>pivot:
             j-=1
         if i<j:
             customlist[i] , customlist[j] = customlist[j] , customlist[i]
     if customlist[i] > pivot:
         customlist[i] , customlist[high] = customlist[high] , customlist[i]
     return i

def quicksort(customlist , low , high):
    if low < high:
        pi = partition(customlist , low , high)
        quicksort(customlist , low , pi-1)
        quicksort(customlist , pi+1 , high)


def arrange_pos_neg(arr , n):
    quicksort(arr , 0 , n-1)
    i,j = 1,1
    while j<n:
        if arr[j] > 0:
            break
        j+=1
    while (arr[i] < 0) and (j<n):
        arr[i] , arr[j] = arr[j] , arr[i]
        i+=2
        j+=1
    return arr

print(arrange_pos_neg(arr , n))