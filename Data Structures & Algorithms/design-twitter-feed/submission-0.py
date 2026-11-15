class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        self.maxHeap = []




    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append((self.count,tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        for user in self.follower[userId] | {userId}:
            for time, tweetid in self.tweets[user]:
                heapq.heappush(maxHeap, (time,tweetid))
        
        res = []
        while maxHeap and len(res) < 10:
            res.append(heapq.heappop(maxHeap)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
