#
# @lc app=leetcode id=37 lang=python
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(memo, i, j): 
            if j == 9:
                i += 1
                j = 0  # 没有return
            if i == 9:  # 这个必须在下面.. 并且没有and j==9
                return True                
            if board[i][j] != '.':
                return dfs(memo, i, j + 1)
            for n in xrange(1, 10):
                cand = set([(i // 3 , j // 3, n), (i + 10, n), \
                    (j + 100, n)])
                if not memo & cand:
                    memo |= cand  # Note 一开始写成cand |= memo....
                    board[i][j] = str(n)
                    if dfs(memo, i, j + 1):
                        return True
                    board[i][j] = '.'
                    memo -= cand
            return False

        memo = set()  # 预先初始化
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != '.':
                    n = int(board[i][j])  # n 必须是0-based.. 
                    memo |= set([(i // 3 , j // 3, n), (i + 10, n), \
                        (j + 100, n)])  # 前面的左边是0-based
        dfs(memo, 0, 0)
        return board
        
if __name__ == '__main__':
    """
    见52题
    嗯编码过程有问题... i + 10是错的.. i + 20就是对的?
    """
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(s.solveSudoku(board))
# @lc code=end

