
# GIVEN AN ARRAY OF 'n' NON-NEGATIVE INTEGERS ,
# EACH REPRESENTING AN ELEVATION MAP ,
# WHERE WIDTH OF EACH BAR IS 1 .
# COMPUTE HOW MUCH WATER COULD BE TRAPPED AFTER RAINING.

from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the array value : "))
    arr.append(temp)

print(f"your array is : {arr}")

def max_water(arr , n):
    result = 0

    for i in range(1 , n-1):
        left = arr[i]
        for j in range(i):
            left = max(left , arr[j])

        right = arr[i]
        for j in range(i+1 , n):
            right = max(right , arr[j])

        result = result + (min(left , right) - arr[i])

    return result

print(max_water(arr , n))
