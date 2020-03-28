class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 72 ms
        # 12.5 MB
        for idx in range(0, 81):
            row, col = idx // 9, idx % 9
            if board[row][col] == ".":
                continue
            small_row, small_col = row // 3, col // 3
            if self.is_row_repeat(board, row) or self.is_col_repeat(board, col) or self.is_small_repeat(board, small_row, small_col):
                return False
        return True

    def is_row_repeat(self, board, small_row):
        visited = set()
        for i in range(0, 9):
            value = board[small_row][i]
            if value == ".":
                continue
            if visited.__contains__(value):
                return True
            visited.add(value)
        return False

    def is_col_repeat(self, board, small_col):
        visited = set()
        for i in range(0, 9):
            value = board[i][small_col]
            if value == ".":
                continue
            if visited.__contains__(value):
                return True
            visited.add(value)
        return False

    def is_small_repeat(self, board, small_row, small_col):
        visited = set()
        for i in range(0, 3):
            for j in range(0, 3):
                value = board[small_row * 3 + i][small_col * 3 + j]
                if value == ".":
                    continue
                if visited.__contains__(value):
                    return True
                visited.add(value)
        return False


if __name__ == "__main__":
    # board =\
    # [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    result = Solution().isValidSudoku(board)
    print("result: {}".format(result))
