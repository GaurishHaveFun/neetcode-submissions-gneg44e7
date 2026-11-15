class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task = Counter(tasks)
        maxHeap = [ -t for t in task.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            if maxHeap:
                one = heapq.heappop(maxHeap) + 1
                if one != 0:
                    q.append((one,time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            time += 1
        
        return time