class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            if i >= len(nums) or sum(path) > target:
                return
            if sum(path) == target:
                res.append(path.copy())
                return
            
            #d1: dont add to path
            backtrack(i + 1)

            #d2: add the next num to path
            path.append(nums[i])
            backtrack(i)
            path.pop()

        backtrack(0)
        return res

