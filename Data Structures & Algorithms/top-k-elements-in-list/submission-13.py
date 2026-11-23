class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        minHeap = []
        hashMap = {}
        res = []

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for key,freq in hashMap.items():
            heapq.heappush(minHeap, (freq,key))
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        
        for freq,key in minHeap:
            res.append(key)
        
        return res


        
        
        
        
        
        
        # nums = [1,2,2,3,3,3], k = 2


        