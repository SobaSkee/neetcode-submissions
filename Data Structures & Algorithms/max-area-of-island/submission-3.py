class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = 0
        def dfs(r,c):
            # if r < 0 or r == N or c < 0 c == M or grid[r][c] == 0 or r,c in visited:
            #     return
            area = 1
            for d in dirs:
                dr, dc = r+d[0], c+d[1]
                if 0 <= dr < N and 0 <= dc < M and grid[dr][dc] == 1:
                    grid[dr][dc] = 0
                    area += dfs(dr,dc)
            return area
            

        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    res = max(res, dfs(r,c))
        return res





