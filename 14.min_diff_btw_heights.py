
# GIVEN A CONSTANT VALUE(k) AN ARRAY - ELEMENTS REPRESENTING THE HEIGHTS
# EITHER BY INCREMENTING OR DECREMENTING THE HEIGHTS BY THE 'k'
# FIND THE MIN DIFF. BTW THE HEIGHTS

from array import *

n = int(input("enter the number of elements : "))
arr = array('i' , [])

for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)

print(arr)

k = int(input("enter the K value : "))


def partition(customlist, low, high):
    i=low
    j=high-1
    pivot=customlist[high]
    while i<j:
        while i<high and customlist[i]<pivot:
            i+=1
        while j>low and customlist[j]>pivot:
            j-=1
        if i<j:
            customlist[i], customlist[j]=customlist[j], customlist[i]
    if customlist[i]>pivot:
        customlist[i], customlist[high]=customlist[high], customlist[i]
    return i


def quicksort(customlist, low, high):
    if low<high:
        pi=partition(customlist, low, high)
        quicksort(customlist, low, pi-1)
        quicksort(customlist, pi+1, high)

def min_height(arr , n , k):
    if (n==1):
        return 0
    quicksort(arr , 0 , n-1)

    ans = arr[n-1] - arr[0]

    small = arr[0] + k
    big = arr[n-1] - k

    if (small > big):
        small , big = big , small

    for i in range(1 , n-1):
        sub = arr[i]-k
        add = arr[i]+k

        if (sub >= small or add <= big):
            continue
        if (big-sub <= add-small):
            small = sub
        else:
            big = add

    return min(ans , (big-small))

print(min_height(arr , n , k))



















