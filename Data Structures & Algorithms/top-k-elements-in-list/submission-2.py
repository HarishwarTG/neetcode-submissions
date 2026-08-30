class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n ,0)

        for key, value in hashmap.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res