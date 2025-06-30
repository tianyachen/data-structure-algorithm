class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)
        minHeap = []
        for authorId in self.following[userId]:
            items = self.user_tweets[authorId]
            for item in items[-10:]:
                heapq.heappush(minHeap, item)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        ans = [tweetId for _, tweetId in sorted(minHeap, reverse = True)]
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)