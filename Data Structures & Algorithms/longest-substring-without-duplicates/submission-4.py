class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindow = 0
        hashSet = set()
        l = 0
        r = 0

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            maxWindow = max(maxWindow, r - l + 1)
        return maxWindow