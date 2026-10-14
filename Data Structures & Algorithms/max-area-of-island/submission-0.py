class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            count = 1

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                row, col = q.popleft()
                for dr, dc in directions: 
                    r = row + dr
                    c = col + dc
                    if (0 <= r < rows and
                        0 <= c < cols and
                        grid[r][c] == 1 and
                        (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))
                        count += 1
            
            return count


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area
