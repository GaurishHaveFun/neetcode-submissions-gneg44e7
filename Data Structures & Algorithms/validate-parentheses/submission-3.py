class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'}':'{', ']':'[', ')':'('}

        for par in s:
            if par in hashMap.keys():
                if stack and stack[-1] == hashMap[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        return len(stack) == 0
