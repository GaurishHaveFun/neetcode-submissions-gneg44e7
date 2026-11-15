class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char.lower())
        
        combined = ''.join(arr)
        return combined == combined[::-1]