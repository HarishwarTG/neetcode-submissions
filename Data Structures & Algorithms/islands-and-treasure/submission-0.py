class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        
        q = collections.deque()

        def addcell(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r,c) in visit or grid[r][c] == -1):
                return
            q.append((r, c))
            visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r + 1, c)
                addcell(r - 1, c)
                addcell(r, c + 1)
                addcell(r, c - 1)

            dist += 1