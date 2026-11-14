class Solution:
    def numSquares(self, n: int) -> int:
        # def dfs(rem) -> remaining is a running amount -> returns minimum
        # Base Case: rem == 0, rem < 0
        # Choices: all the perfect squares(for loop that runs until that number in perfect squares)
        # Combine: Min operator

        memo = {}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return 1e9
            if rem in memo:
                return memo[rem]
            
            res = 1e9
            for i in range(int(math.sqrt(rem)),0,-1):
                res = min(res,1 + dfs(rem - (i*i)))
            memo[rem] = res
            return res
        
        return dfs(n)