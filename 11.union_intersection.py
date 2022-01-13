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
def check_distinct(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(i+1 , len(arr2)):
            if arr1[i] == arr2[j]:
                print("the elements are not distinct")

def i_position(arr , low , high):
    i = low
    j = high-1
    pivot = arr[high]
    while i < j:
        while arr[i] < pivot and i < high:
            i += 1
        while arr[j] > pivot and j >low:
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

intersection_array = array('i' , [])

# union of array
def union_of_array():
    for i in arr2:
        arr1.append(i)

# intersection of array
def intersection_of_array():
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                intersection_array.append(arr1[i])


print(check_distinct(arr1,arr2))

print(quick_sort(arr1 , 0 , -1))
print(quick_sort(arr2 , 0 , -1))

print(union_of_array())
print(f"the union is {arr1}")

print(intersection_of_array())
print(f"the intersion is {intersection_array}")






