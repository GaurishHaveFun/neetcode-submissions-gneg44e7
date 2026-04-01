class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0


        for i in range(len(nums)):
            if nums[i] - 1 not in hashSet:
                count = 1
                while nums[i] + count in hashSet:
                    count += 1
                maxCount = max(maxCount, count)
        return maxCount


        