class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindow = 0
        stack = []
        l = 0
        r = 0

        while r in range(len(s)):
            while s[r] in stack:
                stack.remove(s[l])
                l += 1
            stack.append(s[r])
            r += 1
            maxWindow = max(maxWindow, r - l)
        return maxWindow