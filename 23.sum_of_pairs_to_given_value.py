

def twopairsum(arr , sum):
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i] + arr[j] == sum:
                print(f"the pairs are ({arr[i]},{arr[j]})")

print(twopairsum([1,5,7,1] , 6))
