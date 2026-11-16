class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # We need to return a bool
        # derived[i] = original[i] XOR original[(i + 1) % n]
        # XOR: opposites return 1, same return 0

        n = len(derived)
        original = [0] * n
        original[0] = 0
        
        
        for i in range(0,n-1):
            original[i+1] = derived[i] ^ original[i]

        for i in range(n):
            if original[i] ^ original[(i+1) % n] != derived[i]:
                return False
        return True