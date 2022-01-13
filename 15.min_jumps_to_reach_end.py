
# GIVEN AN ARRAY , ELEMENTS REPRESENTING THE MAX. NUM OF STEPS/JUMPS
# THAT CAN BE MADE FOM THAT ELEMENT.
# FIND THE MIN. NUM OF JUMPS TO REACH THE END OF THE ARRAY
# IF AN ELE IS 0, RETURN -1

from array import *

n = int(input("enter the number of elements : "))
arr = array('i' , [])

for i in range(n):
    temp = int(input("enter the values : "))
    arr.append(temp)

print(arr)

def minjumps(arr , n):
    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    if (n==1):
        return 0
    elif (arr[0]==0):
        return -1
    else:
        for i in range(n):
            if (i==n-1):
                return jumps
            max_reach = max(max_reach , i+arr[i])
            steps -= 1
            if (steps == 0):
                jumps += 1
                if (i >= max_reach):
                    return -1
                steps = max_reach - i

print(minjumps(arr , n))