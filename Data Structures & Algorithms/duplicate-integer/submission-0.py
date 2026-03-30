class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap1 = {}

        for i in range(len(nums)):
            hashMap1[nums[i]] = hashMap1.get(nums[i], 0) + 1
            if hashMap1[nums[i]] > 1:
                return True
        return False