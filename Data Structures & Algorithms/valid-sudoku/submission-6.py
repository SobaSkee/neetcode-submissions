class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in range(len(board)):
            row_entries = []
            for col in range(len(board[0])):
                entry = board[row][col]
                if entry != "." and entry in row_entries:
                    return False
                row_entries.append(entry)
        # check cols
        for col in range(len(board[0])):
            col_entries = []
            for row in range(len(board)):
                entry = board[row][col]
                if entry != "." and entry in col_entries:
                    return False
                col_entries.append(entry)

        # check sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_entries = []
                for i in range(3):
                    for j in range(3):
                        entry = board[box_row+i][box_col+j]
                        if (entry != ".") and (entry in box_entries):
                            return False
                        box_entries.append(entry)

        return True