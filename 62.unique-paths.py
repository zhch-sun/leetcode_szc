#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#
class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     # the m*n space version
    #     # m row n col  # m, n = n, m
    #     dp = [[1] * n for _ in range(m)]  # use 1 for initialization!
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i-1][j] + dp[i][j - 1]
    #     return dp[m - 1][n - 1]
    
    def uniquePaths(self, m, n):
        if m > n:
            m , n = n, m         
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]
        # return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)

if __name__ == '__main__':
    """
    dicuss 里有详细推导过程.
    还可以数学大法
    """
    s = Solution()
    print(s.uniquePaths(7, 3))
        

