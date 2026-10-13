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
        
        l, r = 0, col - 1

        while l <= r:
            mid2 = (l + r) // 2
            if target > matrix[mid][mid2]:
                l = mid2 + 1
            elif target < matrix[mid][mid2]:
                r = mid2 - 1
            else:
                return True
        
        return False