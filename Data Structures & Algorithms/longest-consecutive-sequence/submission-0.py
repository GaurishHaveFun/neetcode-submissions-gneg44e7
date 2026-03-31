class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        count = 0
        maxCount = count

        for i in range(len(nums)):
            if nums[i] - 1 not in hashSet:
                count = 1
                while nums[i] + count in hashSet:
                    count += 1
                maxCount = max(count, maxCount)
        return maxCount
                