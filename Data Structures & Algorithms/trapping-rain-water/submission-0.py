class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res = 0

        l = 0
        r = len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                res = res + abs(max_l - height[l])   
            else:
                r -= 1
                max_r = max(max_r, height[r])
                res = res + abs(max_r - height[r])
                
        return res