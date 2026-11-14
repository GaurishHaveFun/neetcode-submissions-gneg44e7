class Solution:
    def climbStairs(self, n: int) -> int:
        # dfs(i) -> ith step and returns distinct number of ways to reach the top
        # Base Case: Overshoot or exact, i > n or i == n, Overshoot return 0, otherwise return 1
        # Choices: take 1 step or take 2 steps (i+1) or (i+2)
        # Combine: Max/Min, +, in our case + because we want all sorts of ways

        memo = {}
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]
        
        return dfs(0)