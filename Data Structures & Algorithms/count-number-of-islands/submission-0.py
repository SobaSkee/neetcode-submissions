class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        islands = 0

        paths = [(0, 1), (1,0), (0, -1), (-1, 0)]

        def dfs(r,c):
            for path in paths:
                dx = r + path[0]
                dy = c + path[1]
                if 0 <= dx < N and 0 <= dy < M and grid[dx][dy] == '1':
                        grid[dx][dy] = '0'
                        dfs(dx, dy)

        for r in range(N):
            for c in range(M):
                if grid[r][c] == '1':
                    islands += 1
                    grid[r][c] = '0'
                    dfs(r,c)
        return islands

