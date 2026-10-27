class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        ans = []
        heapq.heapify(maxHeap)

        for i in range(len(points)):
            temp = math.sqrt(((points[i][0] - 0)**2) + ((points[i][1] - 0)**2))
            heapq.heappush(maxHeap, [-temp, points[i][0], points[i][1]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            ans.append([x,y])
        return ans
        
        
        
        

        