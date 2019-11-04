#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#
import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)

    # def uniquePaths(self, m, n):
    #     # 初始化第一行第一列, O(m*n) space
    #     # m row n col  # m, n = n, m
    #     dp = [[1] * n for _ in range(m)]  # use 1 for initialization!
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i-1][j] + dp[i][j - 1]
    #     return dp[m - 1][n - 1]
    
    # def uniquePaths(self, m, n):
    #     if m > n:
    #         m , n = n, m         
    #     dp = [1] * n
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[j] = dp[j] + dp[j - 1]
    #     return dp[-1]

    # def uniquePaths(self, m, n):
    #     # 只初始化第一个数
    #     M, N = m, n
    #     if M * N == 0:
    #         return 0
    #     f = [[0] * n for _ in xrange(M)]
    #     f[0][0] = 1
    #     for i in xrange(M):
    #         for j in xrange(N):
    #             if i:
    #                 f[i][j] += f[i-1][j]
    #             if j:
    #                 f[i][j] += f[i][j-1]
    #     return f[-1][-1]

    # def uniquePaths(self, m, n):
    #     M, N = m, n
    #     if M * N == 0:
    #         return 0
    #     f = [0] * N
    #     f[0] = 1
    #     for i in xrange(M):
    #         for j in xrange(N):
    #             if j:
    #                 f[j] += f[j - 1]
    #     return f[-1]

if __name__ == '__main__':
    """
    解法0, 数学大法, 推导过程? 
    解法1/解法2:
        可以初始化第一行第一列, 这样循环内部就不用判断了.
    解法3/解法4:
        更加general, 适合各种情况, 只初始化左上角位置. 
    """
    s = Solution()
    print(s.uniquePaths(7, 3))
        

