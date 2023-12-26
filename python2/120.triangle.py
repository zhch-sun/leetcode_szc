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
    #     # 从上到下, inplace
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
    #     # 从上到下, 滚动数组
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
    #     # 从下到上, n2 space
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
        # 从下到上, O(n) space
        nums = triangle
        if not nums:
            return 0
        N = len(nums)
        f = list(nums[-1])  # [n for n in nums[-1]]
        for i in xrange(N - 2, -1, -1):
            for j in xrange(len(nums[i])):  # Note可以len(g[i])
                f[j] = min(f[j], f[j+1]) + nums[i][j]
        return f[0]

if __name__ == '__main__':
    """
    题设: 给定一个三角形array of array, 找到从上到下的最小和
    结论: 直接从下到上o(n), 不考虑inplace
    解法1: top down
        f[i, j] = min(f[i - 1][j] + f[i - 1][j - 1]) + nums[i][j]
        分类讨论: j=0的时候, 没有j-1, j=END时, 没有j.
        最后还需要min函数.
    解法2: top down O(N2)空间
    解法3: 
        滚动数组: 更general
        发现如果要用滚动数组, 只能从上往下... 否则初始化太困难, 
            1. dp 两行的初始化顺序要根据 N的奇偶性改变
            2. 还要处理N=1的情况. 
        用 &1 替代 mod2, python里面&操作符优先级低于+-
        注意python里面    
    解法4: bottom up O(N2)空间
        f[i, j] = min(f[i + 1][j] + f[i + 1][j + 1])
        不需分类讨论. 最好
        注意两次初始化
    解法5: bottom up O(N)空间
        只用一维的dp即可. 最好的解法. 
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

