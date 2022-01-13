
from array import *

num = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(num):
    temp = int(input("enter the values : "))
    arr.append(temp)
print(arr)

def sortzot(arr , n = len(arr) ):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in range(n):
        if arr[i] == 0:
            count_0 += 1
        if arr[i] == 1:
            count_1 += 1
        if arr[i] == 2:
            count_2 += 1

    for i in range(0,count_0):
        arr[i] = 0
    for i in range(count_0 , count_0+count_1):
        arr[i] = 1
    for i in range(count_0+count_1 , n):
        arr[i] = 2

print(sortzot(arr))
print(arr)