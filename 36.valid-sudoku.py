#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#
class Solution(object):
    # def isValidSudoku(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: bool
    #     """
    #     seen = []
    #     for i, row in enumerate(board):
    #         for j, item in enumerate(row):
    #             if item != '.':
    #                 # Note the tuple
    #                 seen += [(i, item), (item, j), (i/3, j/3, item)]
    #     return True if len(seen) == len(set(seen)) else False

    def isValidSudoku(self, board):
        # 98% early stopping
        seen = set()
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item != '.':
                    for choice in [(i, item), (item, j), (i/3, j/3, item)]:
                        if choice not in seen:
                            seen.add(choice)
                        else:
                            return False
        return True 

if __name__ == '__main__':
    """
    python 的set. update实际就是list版的add. 
    合理的答案确实用hashset来搞比较好. 甚至用一个hashset...
    也可以用三个matrix来搞. 但是这样应该多占内存. 
    也可以用一个list来存所有, 然后转换成set. 看长度. 
    Note: list不能被hash所以不能被set()!! 只有immutable才可以被hash!!
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
