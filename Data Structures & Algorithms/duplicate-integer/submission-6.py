class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()

        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            hashMap.add(nums[i])
        return False