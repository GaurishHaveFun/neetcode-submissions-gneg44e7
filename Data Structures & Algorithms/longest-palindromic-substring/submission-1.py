class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Any upper or lower bound on s? 
        # longestPalindrome -> return longest substring that is palindrome
        # what can s contain of? does the test case "909" a palindrome?
        # can s contain upper and lowercase?
        # can s have 0 length? 
        # If to use a decision tree: what is base case?
        # Base case: len(s) >
        # Sliding Window looks optimal, however how to determine if palindrome
        # What is the constraint on when to move the left pointer?
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        resIdx, resLen = 0, 0

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and (j- i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx:resIdx + resLen]