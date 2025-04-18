def maxProfit(prices):
    """given an array of prices for the day (day = index), find the max profit if you buy and sell"""
    max_profit = 0
    l, r = 0, 1

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1

    return max_profit

print(maxProfit([7,1,5,3,6,4]))