class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones) # inplace
        while len(stones) > 1:
            x = heapq.heappop_max(stones) # 6
            y = heapq.heappop_max(stones) # 4
            if x != y:
                heapq.heappush_max(stones, x - y)
        
        return stones[0] if len(stones) > 0 else 0