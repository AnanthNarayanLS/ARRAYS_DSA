
# TAKE A ARRAY , FIND THE LENGTH OF LARGEST CONSEQUTIVE SUBSEQUENCE..

from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the array value : "))
    arr.append(temp)

print(f"your array is : {arr}")

def find_largest_conseq_sub_seq(arr , n):
    s = set()
    ans = 0

    for i in arr:
        s.add(i)

    for i in range(n):
        if (arr[i] - 1) not in s:
            j = arr[i]
            while (j in s):
                j += 1
            ans = max(ans , j-arr[i])

    return ans

print(find_largest_conseq_sub_seq(arr , n))