class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)

        for num in nums:
            heapq.heappush(maxHeap, num)
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return heapq.heappop(maxHeap)