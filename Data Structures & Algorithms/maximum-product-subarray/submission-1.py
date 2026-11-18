class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            tmp = n * curMax
            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, tmp, curMin * n)
            res = max(res, curMax)
        
        return res