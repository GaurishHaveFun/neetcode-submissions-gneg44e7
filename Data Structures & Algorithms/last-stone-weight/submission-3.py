class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)
            if y > x:
                heapq.heappush(minHeap, (x - y))
        
        minHeap.append(0)
        return abs(minHeap[0])