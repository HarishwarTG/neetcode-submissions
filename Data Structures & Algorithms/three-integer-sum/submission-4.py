class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                break # if no negative, we cant sum to zero
            if i > 0 and n == nums[i - 1]:
                continue # skip duplicate

            l = i + 1
            r = len(nums) - 1
            while l < r:
                isZero = n + nums[l] + nums[r]
                if isZero == 0:
                    res.append([n, nums[l], nums[r]])
                    # once found, move on
                    l += 1
                    r -= 1
                    # skip dup in 2 sum
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif isZero > 0:
                    r -= 1
                elif isZero < 0:
                    l += 1
            
        return res