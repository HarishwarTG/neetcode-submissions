class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        for x in nums:
            if x not in l:
                l.append(x)
            else:
                return True
            
        return False
         