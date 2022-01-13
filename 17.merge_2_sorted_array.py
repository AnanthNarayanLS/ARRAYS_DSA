from array import *

arr1 = array('i', [])
arr2 = array('i', [])
for i in range(2):
    num = int(input("enter the number of values : "))
    for i in range(num):
        temp = int(input("enter the values : "))
        if i == 0:
            arr1.append(temp)
        else:
            arr2.append(temp)

m = len(arr1)
n = len(arr2)

def merge(arr1 , arr2 , m , n):
    for i in range(n-1 , -1 , -1):
        last = arr1[m-1]
        j = m-2
        while (j >= 0 and arr1[j]>arr2[i]):
            arr1[j+1] = arr1[j]
            j-=1
        if (j != m-2 or last > arr2[i]):
            arr1[j+1] = arr2[i]
            arr2[i] = last

merge(arr1 , arr2 , m , n)

print(arr1)
print(arr2)

print("After Merging \nFirst Array:", end="")
for i in range(m):
    print(arr1[i], " ", end="")

print("\nSecond Array: ", end="")
for i in range(n):
    print(arr2[i], " ", end="")