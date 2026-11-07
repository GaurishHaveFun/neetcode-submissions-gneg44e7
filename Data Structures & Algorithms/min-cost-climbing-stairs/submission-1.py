class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Does i have a lower and upper bound? ? <= i <= ?
        # Base cases: When does "top" being considered? is the top the last element in the array? (Top = >last index in cost)
        # We can start on either 0 or 1'st floor
        # Once we are on a floor, we can choose either 1 step or 2 steps

        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        
        return min(dfs(0), dfs(1))