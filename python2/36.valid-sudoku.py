#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """        
        used = set()
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != '.':
                    item = int(board[i][j])
                    cur = {(i + 10, item), (j + 100, item), \
                        (i // 3, j //3, item)}
                    if cur & used:
                        return False
                    used |= cur  # used.update(cur)
        return True

if __name__ == '__main__':
    """
    解法1:
        解决是否出现过的问题，应该用set。。。
        python set的|= 也可以update().
        注意编码只能用加法, 不能用乘法. 
    解法2:
        也可以用四个array来搞. 但是还是set比较简单..
    """
    matrix = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
#     matrix = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
    s = Solution()
    print(s.isValidSudoku(matrix))
