class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        profit = 0
        maxProfit = profit

        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            maxProfit = max(profit, maxProfit)
            r += 1
        return maxProfit

            