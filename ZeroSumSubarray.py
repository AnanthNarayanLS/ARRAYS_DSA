
# to find a subarray with sum equal to zero

from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the array value : "))
    arr.append(temp)

print(f"your array is : {arr}")

def zerosumsubarray(arr , n):
    sum = 0
    s = set()

    for i in range(n):
        sum += arr[i]

        if sum == 0 or sum in s:
            return True
        s.add(sum)
    return False

print(zerosumsubarray(arr , n))
if zerosumsubarray(arr , n) == True:
    print("found a subarray with 0 sum")
else:
    print("no such sub array exists")