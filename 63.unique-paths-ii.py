#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # m row, n col
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n  # Note this 0!
        dp[0] = 1  # Note this 1!
        for i in xrange(0, m):  # or iter with row in obstacleGrid
            for j in xrange(0, n):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j-1]
        return dp[-1]
        

if __name__ == '__main__':
    """
    TODO an inplace implementation
    """
    s = Solution()
    array = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
            ] 
    # array = [[0], [1]]
    print(s.uniquePathsWithObstacles(array))       

