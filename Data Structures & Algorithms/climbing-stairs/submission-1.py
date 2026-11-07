class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 1) Can the steps be taken in any order? like 1 -> 2 = 3 , 2 -> 1 = 3.
        # 2) Assuming n can never be negative, n >= 0, 0 is 0 steps allowed?
        # 3) Is there an upper bound on n? n < ?.
        # 4) Upper Bound = 45, Lower Bound = 1
        # 5) Immediate Solution = Decision Trees (Recursion) DFS
        # 6) Base Case = n>=

        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]

        
        return dfs(0)

