
# Find the Duplicate Number , with constant S.Complex.

from array import *

n = int(input("enter the length of the array : "))
arr = array('i' , [])

for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)

print(arr)

i , j = 0 , 1
while ((i<len(arr)) and (j<len(arr))):
    if (arr[i]==arr[j]):
        print(arr[i])
        break
    elif (j+1 == len(arr)):
        i+=1
        j=i+1
    else:
        j+=1