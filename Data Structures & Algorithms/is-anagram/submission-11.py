class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashMap1[s[i]] = hashMap1.get(s[i], 0) + 1
            hashMap2[t[i]] = hashMap2.get(t[i], 0) + 1
        
        return hashMap1 == hashMap2
