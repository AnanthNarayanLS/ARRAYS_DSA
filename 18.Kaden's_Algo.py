
# Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

from array import *

n = int(input("enter the number of elements : "))
arr = array('i' , [])

for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)

print(arr)

def kadensalgo(arr , n):
    current_sum = 0
    max_sum = 0
    start , end , s = 0,0,0
    for i in range(n):
        current_sum = current_sum + arr[i]
        if (current_sum > max_sum):
            max_sum = current_sum
            start = s
            end = i
        if (current_sum < 0):
            current_sum = 0
            s=i+1
    print(max_sum)
    print(f"the starting index is {start}")
    print(f"the ending index is {end}")

print(kadensalgo(arr , len(arr)))

# ex  :  {1,2,3,-2,5}
# ans :  9