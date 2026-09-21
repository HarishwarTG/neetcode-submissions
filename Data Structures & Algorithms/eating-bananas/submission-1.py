class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l = 1
        r = max(piles)

        while l <= r:
            m = l + ((r - l) // 2)

            total = 0
            for p in piles:
                total += math.ceil(float(p)/m)
            
            if total <= h:
                res = m
                r = m -1
            else:
                l = m + 1
        
        return res
        