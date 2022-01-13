
# FIND THE SUNARRAY OF A GIVEN ARRAY
# WHOSE SUM IS GREATER THAN A GIVEN NUMBER(x)...

from array import *
n = int(input("ENTER THE LENGTH OF THE ARRAY : "))
arr = array('i',[])
for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)

print(arr)

x = int(input("enter the value of X : "))

def smallestsubwithsum(arr , n , x):
    min_len = n+1
    for start in range(0,n):
        curr_sum = arr[start]
        if(curr_sum > x):
            return curr_sum
        for end in range(start+1 , n):
            curr_sum += arr[end]
            if curr_sum > x and (end - start +1)<min_len:
                min_len = (end - start+1)

    return min_len

res = smallestsubwithsum(arr , n , x)
if res == n+1:
    print("NOT POSSOBLE")
else:
    print(res)
