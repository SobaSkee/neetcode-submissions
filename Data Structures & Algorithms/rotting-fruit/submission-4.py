class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        q = deque()
        totalFruit = 0
        rotten = 0


        def rot(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visited:
                return

            grid[r][c] = 2
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    rotten += 1
                if grid[r][c] == 1 or grid[r][c] == 2:
                    totalFruit += 1
        if totalFruit == 0 or rotten == totalFruit:
            return 0
        
        minutes = -1
        while q:
            for i in range(len(q)):
                # coords of rotten fruit
                r,c = q.popleft()
                visited.add((r,c))
                rot(r+1, c)
                rot(r-1, c)
                rot(r, c+1)
                rot(r, c-1)

            minutes += 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
                
        return minutes
        







