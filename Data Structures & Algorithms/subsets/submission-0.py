class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(index):
            if index == len(nums):
                res.append(path.copy())
                return
            #decision 1: add to path
            path.append(nums[index])
            backtrack(index + 1) #recursion on the path
            path.pop() # backtrack the path

            #decision2: dont add to path
            backtrack(index + 1)
            
        backtrack(0)
        return res