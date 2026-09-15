class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        M = len(board[0])

        # check row for dupes
        for r in range(N):
            rowSet = set()
            for c in range(M):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet:
                    return False
                rowSet.add(board[r][c])
        
        # check cols for dupes
        for c in range(M):
            colSet = set()
            for r in range(N):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colSet:
                        return False
                colSet.add(board[r][c])

        # check sub boxes
        for r in range(0, N, 3):
            for c in range(0, M, 3):
                sqSet = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in sqSet:
                            return False
                        sqSet.add(board[i][j])
        return True
