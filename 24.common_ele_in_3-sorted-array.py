
# find common elements In 3 sorted arrays in increasing order

from array import *

arr1 = array('i' , [])
arr2 = array('i' , [])
arr3 = array('i' , [])

for i in range(3):
    n = int(input(f"enter the length of the array{i+1}:"))
    for j in range(n):
        temp = int(input("enter the values : "))
        if i==0:
            arr1.append(temp)
        if i==1:
            arr2.append(temp)
        if i==2:
            arr3.append(temp)

print(arr1)
print(arr2)
print(arr3)

i,j,k=0,0,0
while ((i<len(arr1)) and (j<len(arr2)) and (k<len(arr3))):
    # increment all i,j,k iterators if all the i,j,k values are same
    if ( arr1[i] == arr2[j] == arr3[k] ):
        print(arr1[i])
        i+=1
        j+=1
        k+=1
    # increment only the other 2 iterators
    elif (arr2[j] < arr1[i]) and (arr3[k] < arr1[i]):
        j+=1
        k+=1
    elif (arr1[i] < arr2[j]) and (arr3[k] < arr2[j]):
        i+=1
        k+=1
    elif (arr1[i] < arr3[k]) and (arr2[j] < arr3[k]):
        i+=1
        j+=1
    # increment only 1 iterator
    elif (arr1[i]==arr2[j]) != arr3[k]:
        k+=1
    elif (arr1[i]==arr3[j]) != arr2[j]:
        j+=1
    elif (arr2[i]==arr3[j]) != arr1[i] :
        i+=1















