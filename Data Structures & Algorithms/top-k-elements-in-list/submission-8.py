class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        freqsorted = sorted(freq.keys(), key = lambda x: freq[x], reverse = True)
        return freqsorted[:k]



