
from array import *

arr1 = array('i' , [])
arr2 = array('i' , [])
for i in range(1):
    n = int(input("enter the number of values : "))
    for i in range(n):
        temp = int(input("enter the array value : "))
        if i == 0:
            arr1.append(temp)
        else:
            arr2.append(temp)
print(f"your array 1 is : {arr1}")
print(f"your array 2 is : {arr2}")

def is_subset(arr1 , arr2 , m = len(arr1) , n = len(arr2)):
    i,j = 0,0
    if m < n:
        return 0

    arr1.sort()
    arr2.sort()

    while i < n and j < m:
        if arr1[j] < arr2[i]:
            j+=1
        elif arr1[j] == arr2[i]:
            j+=1
            i+=1
        elif arr1[j] > arr2[i]:
            return 0
    return False if i<n else True

print(is_subset(arr1 , arr2 , m , n))

if (is_subset(arr1 , arr2 , m , n)) == True:
   print("arr2 is a SS of arr1")
else:
   print("arr2 is a SS of arr1")