#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
# class Solution(object):
#     def solve(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """
#         def dfs(i, j):
#             # 也可以是if board[i][j] == 'O'
#             if board[i][j] == '#' or board[i][j] == 'X': 
#                 return
#             board[i][j] = '#'
#             dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#             for d in dirs:
#                 ni = i + d[0]
#                 nj = j + d[1]
#                 # if 0 <= ni < m  and 0 <= nj < n:
#                 if 0 < ni < m - 1  and 0 < nj < n - 1:  # 避免recursive爆栈..
#                     dfs(ni, nj)

#         m = len(board)
#         if m == 0:
#             return
#         n = len(board[0])
#         # if n == 0:  # 这个不需要, 下面自动满足这个条件
#         #     return
        
#         for row in [0, m-1]:
#             for col in range(n):
#                 dfs(row, col)

#         for col in [0, n-1]:
#             for row in range(m):
#                 dfs(row, col)

#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'O':  # 同时转换两种情况
#                     board[i][j] = 'X'
#                 elif board[i][j] == '#':
#                     board[i][j] = 'O'
        
#         return board
        
class UF(object):
    # weighted quick union
    def __init__(self, N):
        self.id = list(range(N))
        self.sz = [1] * N

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

    def find(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution(object):
    def solve(self, board):
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        uf = UF(m * n + 1)
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) \
                    and board[i][j] == 'O':
                    uf.union(i * n + j, m * n)
                elif board[i][j] == 'O':
                    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni = i + d[0]
                        nj = j + d[1]
                        if board[ni][nj] == 'O':
                            uf.union(ni * n + nj, i * m + j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not uf.connected(i * n + j, m * n):
                    board[i][j] = 'X'
        
        return board


if __name__ == '__main__':
    """
    解法1 dfs:
        就是先循环每条边, 遇到o就把连着o的全都赋值成 *. 
        然后把剩下的o都变成x, 剩下的*变回O
        corner case1: 只需要check m, 不需要check n. 
        corner case2: recursion会爆栈!! 而且即使我修改后的答案还是会爆栈.. 见答案下面第一个评论
        https://leetcode.com/problems/surrounded-regions/discuss/41612/A-really-simple-and-readable-C%2B%2B-solutionuff0conly-cost-12ms 
    解法2: iterative dfs:
        https://leetcode.com/problems/surrounded-regions/discuss/41630/9-lines-Python-148-ms
        就是第一步的时候, 把所有边界push进去, 然后如果一个边界是'O', 再把相邻四个push进去. 
        需要一些奇技淫巧.. 不写了. 
    解法3: union find
        需要把所有边上的O连到一个dummyhead上. 
        对于内部的O, 就把它和四周的O连在一起... 真巧妙....
        还有注意是i * n + j 不是i * m + j....
    """
    s = Solution()
    X = 'X'
    O = 'O'
    board = [
        [X, X, X, X],
        [X, O, O, X],
        [X, X, O, X],
        [X, O, X, X],
    ]
    print(s.solve(board))
