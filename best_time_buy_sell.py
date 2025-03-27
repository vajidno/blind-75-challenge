def bestTimeBuySell(arr:list[int])->int:
    buy,sell = 0,1
    max_profit = 0
    while sell<len(arr):
        if arr[sell]>arr[buy]:
            profit = arr[sell]-arr[buy]
            max_profit = max(profit,max_profit)
        else:
            buy = sell
        sell+=1
    return max_profit

print(bestTimeBuySell([7,1,5,3,6,4]))        

