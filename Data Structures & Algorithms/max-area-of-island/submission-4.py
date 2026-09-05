class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        res = 0
        q = deque()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def destroy(x, y):
            
            if x < 0 or y < 0 or x == N or y == M or grid[x][y] == 0:
                return 0
            area = 1
            grid[x][y] = 0
            q.append([x, y])
            for d in dirs:
                newX, newY = x + d[0], y + d[1]
                area += destroy(newX, newY)
            
            return area



        for i in range(N):
            for j in range(M):
                # find islands and add to q
                if grid[i][j] == 1:
                    q.append([i,j])
                    
        
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                res = max(res, destroy(x, y))

        return res


