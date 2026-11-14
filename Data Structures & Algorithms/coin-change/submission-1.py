class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def dfs(i) -> ith index of coins -> return minimum number of coins
        # Base Case: 2 base cases: amount = tempTarget or tempTarget > amount
        # Choices: Take the dollar amount or skip it and move onto next
        # Combine: Min, have to use min operator since we need fewest coins

        memo = {}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return 1e9
            if rem in memo:
                return memo[rem]
            
            res = 1e9
            for coin in coins:
                memo[rem] = min(res, 1 + dfs(rem - coin))
                res = memo[rem]
            return res

        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
