class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = ''.join(sorted(s))
        w2 = ''.join(sorted(t))

        return w1 == w2