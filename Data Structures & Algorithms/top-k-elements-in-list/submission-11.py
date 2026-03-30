class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        heap = []
        res = []

        for i in range(len(nums)):
            freqCount[nums[i]] = freqCount.get(nums[i], 0) + 1

        for key, freq in freqCount.items():
            heapq.heappush(heap, (freq, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for freq, value in heap:
            res.append(value)
        return res

