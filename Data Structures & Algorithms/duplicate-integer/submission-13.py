class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl_del = set(nums)

        return len(nums) != len(dupl_del)