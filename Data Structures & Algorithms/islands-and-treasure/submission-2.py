class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        N = len(grid)
        M = len(grid[0])

        visited = set()
        q = deque()

        def addCell(r,c):
            if r < 0 or r == N or c < 0 or c == M or (r,c) in visited or grid[r][c] == -1:
                return
            
            q.append([r,c])
            visited.add((r,c))

        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            dist += 1


                