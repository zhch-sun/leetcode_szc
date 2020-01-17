#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
from itertools import chain
class Solution(object):
    # def exist(self, board, word):
    #     # 标准写法, 需要修改board
    #     def dfs(i, j, k):
    #         if board[i][j] != word[k]:
    #             return False
    #         if k == len(word) - 1:
    #             return True
    #         tmp, board[i][j] = board[i][j], ''               
    #         for d in dirs:
    #             ni = i + d[0]
    #             nj = j + d[1]
    #             if 0 <= ni < M and 0 <= nj < N:
    #                 if dfs(ni, nj, k + 1):
    #                     return True
    #         board[i][j] = tmp
    #         return False

    #     if not word:
    #         return True
    #     if not board or not board[0]:
    #         return False
    #     M, N = len(board), len(board[0])
    #     dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    #     for i in xrange(M):
    #         for j in xrange(N):
    #             if dfs(i, j, 0):
    #                 return True
    #     return False

    def exist(self, board, word):
        # set存储路径
        def dfs(i, j, k, tmp):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp.add((i, j))
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in tmp:
                    if dfs(ni, nj, k + 1, tmp):
                        return True
            tmp.remove((i, j))
            return False

        if not word:
            return True
        if not board or not board[0]:
            return False
        M, N = len(board), len(board[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for i in xrange(M):
            for j in xrange(N):
                if dfs(i, j, 0, set()):
                    return True
        return False

if __name__ == '__main__':
    """
    题设: 
        二维棋盘上搜索字符串, 字符不能重用, 返回是否存在. 
        212th. 在棋盘上找字典上的字符串是否存在.
        坑: 
            1. 字符是否可以重用: 是否需要记录or暂时赋None
            2. 是否可以修改原matrix: 不能的话其实copy一个即可, 复杂度一样
    复杂度: 
        时间MN * 3^k. k是word长度, 空间O(N2)
    解法1:
        最简单写法, 需要修改matrix, 
        走过的路赋值为奇怪的东西, 但是其实用同样大小的memory. 
        如果找到, 因为return True会直接返回, 所以之前路径的board的值来不及改回来.
    解法2:  
        用set储存之前的路径, 居然更快 300ms->290ms
        for循环+backtrack. 用list/ set存着之前走过的路径, set实际会快很多 
        TODO dirs应该是tuple of tuple? 
        但是有若干细节需要注意: 运动方向需要可行. 上下左右都不能越界
    解法3: 
        不管
        若干剪枝, 判断k>N2 : 更慢
        循环之前check棋盘是否含有有所有字符: 可以用set的<=操作符, 也慢?
        loop unrollling: 最快.
    """
    s = Solution()
    board = \
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    print(s.exist(board, "ABCCED"))
    # print(s.exist(board, "SEE"))
    # print(s.exist(board, "ABCB"))

    # board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
    # print(s.exist(board, "aaaaaaaaaaab"))

    # board = [["a","a"]]
    # print(s.exist(board, "aaa"))
