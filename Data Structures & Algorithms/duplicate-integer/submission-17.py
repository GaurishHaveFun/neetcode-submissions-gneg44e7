class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupe = set(nums)

        return len(nums) != len(noDupe)

        