class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set) # {fr_id: (fe_id1, fe_id2)}
        self.tweets = defaultdict(list) # {userid: [t1, t2]}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1 # add timestamp
        self.tweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        heapq.heapify_max(maxHeap)

        users = self.following[userId] | {userId} # set union to add own self
        for user in users:
            for time, tweet in self.tweets[user]:
                heapq.heappush_max(maxHeap, (time, tweet))
        #         maxHeap.append((time, tweet))
        # heapq.heapify_max(maxHeap)

        while maxHeap and len(res) < 10:
            time, tweet = heapq.heappop_max(maxHeap)
            res.append(tweet)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: # dont add own self
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId) # discard will not throw if user not followed else use remove with if check
