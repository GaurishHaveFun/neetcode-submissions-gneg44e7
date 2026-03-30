class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        valuesSorted = sorted(freq.keys(), key= lambda x: freq[x])
        return valuesSorted[-k:]