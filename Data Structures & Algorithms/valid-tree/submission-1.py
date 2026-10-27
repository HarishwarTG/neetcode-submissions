class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        q = collections.deque([(0, -1)])
        visit.add(0)

        while q:
            i, prev = q.popleft()

            for j in adj[i]:
                if j == prev:
                    continue
                if j in visit:
                    return False
                visit.add(j)
                q.append((j, i))

        return n == len(visit)