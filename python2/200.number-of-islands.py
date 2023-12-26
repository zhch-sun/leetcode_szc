#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#
class UF(object):
    def __init__(self, N):
        self.id = list(range(N))
        self.sz = [1] * N
        self.count = N

    def find(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p
                                                          
    def union(self, p, q):
        i = self.find(p)  # Note 这里写成self.id[p]了....
        j = self.find(q) 
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = self.id[j]
            self.sz[j] += self.sz[i]            
        else:
            self.id[j] = self.id[i]
            self.sz[i] += self.sz[j]
        self.count -= 1    

class Solution(object):
    # def numIslands(self, grid):
    #     """
    #     :type grid: List[List[str]]
    #     :rtype: int
    #     """
    #     m = len(grid)
    #     if m == 0:
    #         return 0
    #     n = len(grid[0])
    #     uf = UF(m * n)
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == '0':
    #                 uf.count -= 1
    #             if grid[i][j] == '1':
    #                 for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    #                     ti = i + d[0]
    #                     tj = j + d[1]
    #                     if 0 <= ti < m and 0 <= tj < n and grid[ti][tj] == '1':
    #                         uf.union(n * i + j, n * ti + tj)
    #     return uf.count

    # def numIslands(self, grid):
    #     def dfs(i, j):
    #         grid[i][j] = '0'
    #         dirs = ((1,0), (-1, 0), (0, 1), (0, -1))
    #         for d in dirs:
    #             ti, tj = i + d[0], j + d[1]
    #             if 0 <= ti < M and 0 <= tj < N and grid[ti][tj] == '1':
    #                 dfs(ti, tj)

    #     if not grid or not grid[0]:
    #         return 0
    #     M, N = len(grid), len(grid[0])
    #     cnt = 0
    #     for i in xrange(M):
    #         for j in xrange(N):
    #             if grid[i][j] == '1':
    #                 dfs(i, j)
    #                 cnt += 1
    #     return cnt

    def numIslands(self, grid):
        def bfs(i, j):
            dirs = ((1,0), (-1, 0), (0, 1), (0, -1))
            dq = deque([(i, j)])
            grid[i][j] = '0'
            while dq:
                ci, cj = dq.pop()
                for d in dirs:
                    ti, tj = ci + d[0], cj + d[1]
                    if 0 <= ti < M and 0 <= tj < N and grid[ti][tj] == '1':
                        grid[ti][tj] = '0'
                        dq.append((ti, tj))

        from collections import deque
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])
        cnt = 0
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j] == '1':
                    bfs(i, j)
                    cnt += 1
        return cnt

if __name__ == '__main__':
    """
    解法1: union find: 
        注意'0'不算在count内, 一个简单的方法是循环的时候遇到0减1!!!自己想出的.
        速度还是慢..
    解法2: dfs
        用dfs探索, 注意要把已经探索过的island上所有的1都赋值为0. 
        注意还是有可能爆栈. 也可以搞成iterative的. 128
    解法3: bfs
        为什么popleft 会 TLE???
        因为必须在入队时标记已经访问过. 
        出队时标记会TLE!!!
    """
    s = Solution()
    grid = [
        [c for c in '11000'],
        [c for c in '11000'],
        [c for c in '00100'],
        [c for c in '00011'],
    ]
    grid = [
        ["1","0","1","1","1"],\
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]]
    print(s.numIslands(grid))

