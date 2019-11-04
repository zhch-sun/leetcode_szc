#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#
class Solution(object):
    # def minimumTotal(self, triangle):
    #     """
    #     :type triangle: List[List[int]]
    #     :rtype: int
    #     """
    #     # top-down inplace
    #     g = triangle
    #     if not g:
    #         return 0
    #     N = len(g)
    #     for i in xrange(1, N):
    #         for j in xrange(len(g[i])):
    #             if j == 0:
    #                 g[i][j] += g[i - 1][j]
    #             elif j == len(g[i]) - 1:  # Note -1!!!
    #                 g[i][j] += g[i - 1][j - 1] 
    #             else:
    #                 g[i][j] += min(g[i-1][j], g[i-1][j-1])
    #     return min(g[-1])

    # def minimumTotal(self, triangle):
    #     """
    #     :type triangle: List[List[int]]
    #     :rtype: int
    #     """
    #     # 从上到下, O(n2)空间
    #     g = triangle
    #     if not g:
    #         return 0
    #     N = len(g)
    #     f = [[0] * len(g[i]) for i in xrange(N)]  # Note 初始化哟
    #     f[0][0] = g[0][0]
    #     for i in xrange(1, N):
    #         for j in xrange(len(g[i])):
    #             if j == 0:
    #                 f[i][j] = f[i - 1][j] + g[i][j]
    #             elif j == len(g[i]) - 1:  # Note -1!!!
    #                 f[i][j] = f[i - 1][j - 1] + g[i][j]
    #             else:
    #                 f[i][j] = min(f[i-1][j], f[i-1][j-1]) + g[i][j]
    #     return min(f[-1]) 

    # def minimumTotal(self, triangle):
    #     """
    #     :type triangle: List[List[int]]
    #     :rtype: int
    #     """
    #     # 滚动数组, 从上到下
    #     g = triangle
    #     if not g:
    #         return 0
    #     N = len(g)
    #     f = [[0] * N for i in xrange(2)]  # Note 初始化啊啊啊啊. 
    #     f[0][0] = g[0][0]
    #     for i in xrange(1, N):
    #         for j in xrange(len(g[i])):
    #             if j == 0:
    #                 f[i&1][j] = f[i - 1&1][j] + g[i][j]
    #             elif j == len(g[i]) - 1:  # Note -1!!!
    #                 f[i&1][j] = f[i - 1&1][j - 1] + g[i][j]
    #             else:
    #                 f[i&1][j] = min(f[i-1&1][j], f[i-1&1][j-1]) + g[i][j]
    #     return min(f[N - 1 & 1])

    # def minimumTotal(self, triangle):
    #     # bottom up inplace
    #     g = triangle
    #     if not g:
    #         return 0
    #     N = len(g)
    #     for i in xrange(N - 2, -1, -1):  # 从倒数第二行开始
    #         for j in xrange(len(g[i])):
    #             g[i][j] += min(g[i+1][j], g[i+1][j+1])
    #     return g[0][0]
    
    # def minimumTotal(self, triangle):
    #     # n2 space
    #     g = triangle
    #     if not g:
    #         return 0
    #     N = len(g)
    #     f = [[0] * len(g[i]) for i in xrange(N - 1)]  # Note 初始化哟
    #     f.append(g[-1])  # Note 另一个初始化, 其实是错误的, 会指针过去..
    #     for i in xrange(N - 2, -1, -1):
    #         for j in xrange(len(g[i])):
    #             f[i][j] = min(f[i+1][j], f[i+1][j+1]) + g[i][j]
    #     return f[0][0]

    def minimumTotal(self, triangle):
        # O(n) space
        g = triangle
        if not g:
            return 0
        N = len(g)
        f = [n for n in g[-1]]
        for i in xrange(N - 2, -1, -1):
            for j in xrange(len(g[i])):
                f[j] = min(f[j], f[j+1]) + g[i][j]
        return f[0]

if __name__ == '__main__':
    """
    题设: 给定一个三角形array of array, 找到从上到下的最小和
    解法1: top down
        对于i,j,上面的两个值分别为i-1,j和i-1,j-1. 
        j=0的时候, 没有j-1, j=END时, 没有j.
        算法问题在于
            1. 需要三个分类讨论
            2. 最后还需要一个min函数
    解法2: top down O(N2)空间
    解法2: bottom up
        好处是, 循环中不需要分类讨论, 最后也不需要min. 
        因为循环变量是越来越小的, 一定可以索引到之前的地方. 
        第一个解法是inplace
    解法3: O(N2)空间
        注意两次初始化
    解法4: O(N)空间
        只用一维的dp即可. 最好的解法. 
    解法5: 
        滚动数组: 更general
        发现如果要用滚动数组, 只能从上往下... 初始化太困难, 
            1. dp 两行的初始化顺序要根据 N的奇偶性改变
            2. 还要处理N=1的情况. 
        用 &1 替代 mod2, python里面&操作符优先级低于+-
        注意python里面
    """
    s = Solution()
    array = [
               [2],
              [3,4],
             [6,5,7],
            [4,1,8,3]
            ]
    # array = [[-10]]
    print(s.minimumTotal(array))

