
from array import *

n = int(input("enter the number of values : "))
arr = array('i' , [])
for i in range(n):
    temp = int(input("enter the array value : "))
    arr.append(temp)

print(f"your array is : {arr}")

class solutions:
    def swap(self , nums , index1 , index2):
        nums[index1] , nums[index2] = nums[index2] , nums[index1]

    def reverse(self , nums , begin , end):
        while begin < end:
            self.swap(nums , begin , end)
            begin += 1
            end -= 1

    def nextpermutations(self , nums):
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swap(nums , 0 , 1)

        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec+1]:
            dec -= 1

        self.reverse(nums , dec+1 , len(nums)-1)

        if dec == -1:
            return

        next_num = dec+1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        self.swap(nums , next_num , dec)
        return nums

sol = solutions()
print(sol.nextpermutations(arr))