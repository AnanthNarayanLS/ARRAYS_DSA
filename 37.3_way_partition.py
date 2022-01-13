
# GIVEN AN ARRAY OF SIZE n AND A RANGE [a,b]
# PARTITION HE ARRAY IN SUCH A WAY THAT ;
# 1.ALL ELE < a APPEAR 1ST
# 2.ALL THE ELE BTW THE RANGE (a,b) APPEAR NEXT
# 3.ALL THE ELE >b APPEAR AT THE END.

from array import *
n = int(input("ENTER THE LENGTH OF THE ARRAY : "))
arr = array('i',[])
for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)

print(arr)

a = int(input("enter the value of lower range : "))
b = int(input("enter the value of upper range : "))

def threewaypartiotion(arr , a , b , n):

    start , end , i = 0 , n-1 , 0

    while (i<=end):
        if (arr[i] <= a):
            arr[i] , arr[start] = arr[start] , arr[i]
            i+=1
            start += 1

        elif (arr[i] >= b):
            arr[i], arr[end]=arr[end], arr[i]
            end-=1
        else:
            i+=1

threewaypartiotion(arr , a, b , n)
print(arr)
