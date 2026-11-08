class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxString = ''
        for l in range(len(s)):
            tmpString = ''
            for r in range(l,len(s)):
                tmpString += s[r]
                if (len(tmpString) > len(maxString)) and (tmpString[::-1] == tmpString):
                    maxString = tmpString
        return maxString