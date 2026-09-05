class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            area = 1

            for d in dirs:
                dx, dy = r+d[0], c+d[1]
                if 0 <= dx < N and 0 <= dy < M and grid[dx][dy] == 1:
                    grid[dx][dy] = 0
                    area += dfs(dx, dy) 
            return area

        res = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    res = max(dfs(r, c), res)
        return res

