# 36. 有效的数独
# https://leetcode-cn.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 暴力方法??
        # 还有其它解法吗?
        # 可以进行一次迭代吗?
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        box = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                curNum = ord(board[i][j]) - ord('0')
                if row[i][curNum] != 0 or col[j][curNum] != 0 or box[j // 3 + (i // 3) * 3][curNum] != 0:
                    return False
                row[i][curNum], col[j][curNum],box[j // 3 + (i // 3) * 3][curNum] = 1, 1, 1
        return True

