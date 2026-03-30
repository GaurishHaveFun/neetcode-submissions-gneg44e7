class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            comp = numbers[l] + numbers[r]
            if target < comp:
                r -= 1
            elif target > comp:
                l += 1
            else:
                return [l + 1, r + 1]
