class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset = set(nums)

        if len(dupset) != len(nums):
            return True
        return False