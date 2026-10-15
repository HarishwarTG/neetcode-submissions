class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        dist = 0
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c, dist))
        
        while q:
           row, col, dist = q.popleft()
           for dr, dc in directions:
            r = row + dr
            c = col + dc
            if (0 <= r < rows and 0 <= c < cols and
                grid[r][c] == 2147483647):
                grid[r][c] = dist + 1
                q.append((r,c, dist + 1))
                    