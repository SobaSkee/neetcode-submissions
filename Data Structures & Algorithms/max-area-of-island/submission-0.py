class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        
        paths = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0

        def dfs(r,c):
            grid[r][c] = 0
            area = 1
            for path in paths:
                dx = r + path[0]
                dy = c + path[1]
                if 0 <= dx < N and 0 <= dy < M and grid[dx][dy] == 1:
                    area += dfs(dx, dy)
            return area
        
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    total = dfs(r,c)
                    res = max(res, total)
        return res







