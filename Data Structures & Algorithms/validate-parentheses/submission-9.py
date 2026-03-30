class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')' : '(', ']':'[','}':'{'}
        stack = []

        for i in range(len(s)):
            if s[i] not in hashMap:
                stack.append(s[i])
            else:
                if stack and hashMap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0