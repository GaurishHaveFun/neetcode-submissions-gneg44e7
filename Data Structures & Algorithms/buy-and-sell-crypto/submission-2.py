class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxProfit = profit
        l = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            maxProfit = max(maxProfit, profit)
        return maxProfit