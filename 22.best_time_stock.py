

def maxprofit(arr):
    left , right = 0 ,1
    max_profit = 0

    while right < len(arr):
        if arr[left] < arr[right]:
            profit = arr[right] - arr[left]
            max_profit = max(profit , max_profit)
        else:
            left = right
        right += 1

    return max_profit
