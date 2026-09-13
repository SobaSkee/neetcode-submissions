class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        M = len(board[0])

        # check rows for dupes
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
        # r: 0, c: 0-8, colSet = ()
        
        # check 3x3 has no dupes
        for r in range(0, N, 3):
            for c in range(0, M, 3):
                squareSet = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in squareSet:
                            return False
                        squareSet.add(board[i][j])
        return True
"""
["1","2",".",".","3",".",".",".","."]
["4",".",".","5",".",".",".",".","."]
[".","9","1",".",".",".",".",".","3"]
["5",".",".",".","6",".",".",".","4"]
[".",".",".","8",".","3",".",".","5"]
["7",".",".",".","2",".",".",".","6"]
[".",".",".",".",".",".","2",".","."]
[".",".",".","4","1","9",".",".","8"]
[".",".",".",".","8",".",".","7","9"]


"""
                