#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#
class Solution(object):
    # def minPathSum(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     m, n = len(grid), len(grid[0])
    #     dp = list(grid[0])  # note this makes a copy!
    #     for j in range(1, n):
    #         dp[j] = dp[j-1] + dp[j]
    #     for i in range(1, m):  
    #         dp[0] = dp[0] + grid[i][0]
    #         for j in range(1, n):
    #             dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
    #     return dp[-1]
    
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1, m):  
            grid[i][0] = grid[i][0] + grid[i-1][0]
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]

if __name__ == '__main__':
    """
    这样只初始化第一行, 不初始化第一列是一个相对好的方案. 95%
    直接用grid更简单, 一个二维的dp
    """
    s = Solution()
    array = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    print(s.minPathSum(array))
