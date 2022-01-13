
# MEDIAN OF 2 SORTED ARR

from array import *
n1= int(input("ENTER THE LENGTH OF THE ARRAY 1 : "))
arr1 = array('i',[])
for i in range(n1):
    temp1 = int(input("enter the values : "))
    arr1.append(temp1)

n2 = int(input("ENTER THE LENGTH OF THE ARRAY 2 : "))
arr2 = array('i',[])
for i in range(n2):
    temp2 = int(input("enter the values : "))
    arr2.append(temp2)

print(arr1)
print(arr2)

def medianof2sortarr(n1 , n2 , arr1 , arr2):

    if (n1%2 != 0) and (n2%2 != 0):
        med1 = int(n1/2)
        med2 = int(n2/2)
    else:
        med1 = int((n1/2)-1)
        med2 = int((n2/2)-1)

    med_sorted = (arr1[med1]+arr2[med2])/2
    print(f"the median of sorted array is {med_sorted}")

print(medianof2sortarr(n1 , n2 , arr1 , arr2))