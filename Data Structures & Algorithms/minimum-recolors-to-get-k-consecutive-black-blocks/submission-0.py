class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        whites = 0

        for i in range(k):
            if blocks[i] == 'W':
                whites += 1
        
        best = whites
        l = 0

        for r in range(k,len(blocks)):
            if blocks[r] == 'W':
                whites += 1
            if blocks[l] == 'W':
                whites -= 1
            l += 1
            best = min(best,whites)
        
        return best
            
            