class Solution:
    def rob(self, nums: List[int]) -> int:
        # Where should robbing start? left --> right , start at max(0 or 1)
        # Base case = when len(nums). i >= len(nums)
        # i any upper or lower bounds? can i be negative? assume no
        # i upper bound >= len(nums), there are only len(nums) houses
        # dfs(i) -> maximum amount of money (integer)

        memo = [-1] * len(nums)
        
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max((nums[i] + dfs(i+2)), dfs(i+1))
            return memo[i]
        
        return dfs(0)