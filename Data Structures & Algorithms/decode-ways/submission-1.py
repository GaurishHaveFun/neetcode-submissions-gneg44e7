class Solution:
    def numDecodings(self, s: str) -> int:
        # First thoughts was hashmap, however it wants number of ways to decode it
        # Decision Trees seem like a smart way to break it into smaller subproblems
        # What is the base case though? When we run out of len(s)
        # The key distinction is new ways only occur after 9. 9 > 
        # dfs(s) -> Returns number of ways to decode
        # 2 choices = stay with the number or add the next consecutive number 

        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            
            res = dfs(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            
            memo[i] = res
            return res
        
        return dfs(0)
            