
# GIVEN AN ARRAY OF 'N' ELEMENTS AND 'M' NUM OF STUDENTS
# WHERE EACH ELE REPRESENTS A PACKET WITH CHOCOLATES
# WHERE NUM OF CHOCOLATES CORRESPONDS TO THE VALUE OF ELE IN THE ARRAY
# UR WORK - *Each student gets one packet.
#           *The difference between the
#            number of chocolates in the packet with maximum chocolates and
#            packet with minimum chocolates
#            given to the students is minimum.

from array import *
n = int(input("ENTER THE LENGTH OF THE ARRAY : "))
arr = array('i',[])
for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)

print(arr)

m = int(input("enter the value of m : "))


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

def findmindiff(arr , n , m):
    if (m==0 or n==0):
        return
    quicksort(arr , 0 , n-1)

    if(n<m):
        return -1

    min_diff = arr[n-1] - arr[0]

    for i in range(len(arr) - (m+1)):
        min_diff = min(min_diff , arr[i+m-1]-arr[i])
    return min_diff

print(findmindiff(arr , n , m))