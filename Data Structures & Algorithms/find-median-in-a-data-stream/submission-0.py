class MedianFinder:

    def __init__(self):
        self.small = [] # max Heap
        self.large = [] # min Heap

    def addNum(self, num: int) -> None:
        #1. push to small
        heapq.heappush_max(self.small, num)
        #2. move the larger val
        val = heapq.heappop_max(self.small)
        heapq.heappush(self.large, val)
        #3.balance, small should have 1 more val
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.small[0] + self.large[0]) / 2
        else:
            return self.small[0]
        