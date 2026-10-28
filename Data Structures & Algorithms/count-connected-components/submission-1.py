class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        res = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(i):
            for j in adj[i]:
                if not visit[j]:
                    visit[j] = True
                    dfs(j)
        
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1
            
        return res