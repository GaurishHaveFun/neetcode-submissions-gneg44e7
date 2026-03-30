class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        arr = sorted(freq.keys(), key = lambda k: freq[k], reverse = True) 

        return  arr[:k]