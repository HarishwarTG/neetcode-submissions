class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [ [] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[b] += 1
            adj[a].append(b)
        
        q = collections.deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        res = []
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if finish != numCourses: return []
        return res[::-1]