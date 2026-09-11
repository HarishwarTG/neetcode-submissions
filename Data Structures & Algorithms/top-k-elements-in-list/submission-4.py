class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for key, value in hashmap.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if k == len(res):
                    return res