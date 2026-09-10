class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row - 1
        
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l, r = 0, col - 1

        while l <= r:
            middle = (l+r) // 2
            if target > matrix[mid][middle]:
                l = middle + 1
            elif target < matrix[mid][middle]:
                r = middle - 1
            elif target == matrix[mid][middle]:
                return True
        
        return False