from typing import List

def maxProfit(prices):
    l = res = 0
    r = 1
    
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] = prices[l]
            res = max(res, profit)
        else:
            l = r
        r += 1
        
    return res