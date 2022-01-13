
# GIVEN AN ARRAY OF SIZE 'n' AND A NUM 'k'
# APPLY ANY NUM OF SWAPPING OPERATION ON THE ARRAY
# AND BRING THE ELE'S (<K) TO ONE SIDE OF ARRAY
# AND PRINT THE MIN. NUM OF SWAPS


from array import *
n = int(input("ENTER THE LENGTH OF THE ARRAY : "))
arr = array('i',[])
for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)

print(arr)

k = int(input("enter the value of K : "))


def minswapsk(arr , n , k):

    start , end , i = 0 , n-1 , 0
    swap_count = 0
    while (i <= end):
        if (i < k):
            i+=1
        elif (i >= k) and (end <= k):
            arr[i] , arr[end] = arr[end] , arr[i]
            swap_count += 1
            end -= 1
            i+=1
        else:
            end-=1
    return swap_count
    return arr

print(minswapsk(arr , n , k))
