class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify_max(maxHeap)
        res = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush_max(maxHeap, [dist, x, y])
            while len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        while len(maxHeap):
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res
