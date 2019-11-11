#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nums = grid
        M, N = len(nums), len(nums[0])
        dp = list(nums[0])  # note this makes a copy!
        for j in range(1, N):  # 初始化第一行.
            dp[j] = dp[j-1] + dp[j]
        for i in range(1, M):  
            dp[0] = dp[0] + nums[i][0] # 处理第一列的情况. 
            for j in range(1, N):
                dp[j] = min(dp[j], dp[j-1]) + nums[i][j]
        return dp[-1]

    # def minPathSum(self, grid):
    #     # f[i][j] = min(f[i-1][j], f[i][j-1]) + nums[i][j]
    #     # f[j] = min(f[j], f[j-1]) + nums[i][j]
    #     nums = grid
    #     M, N = len(nums), len(nums[0])
    #     f = [float('inf')] * (N + 1)  # 0初始化不是intMax
    #     f[1] = nums[0][0]
    #     for i in xrange(1, M + 1):
    #         for j in xrange(1, N + 1):
    #             if i > 1 or j > 1:
    #                 f[j] = min(f[j], f[j - 1]) + nums[i-1][j-1]
    #     return f[-1]

if __name__ == '__main__':
    """
    思路: DP
        f[i][j] = min(f[i-1][j], f[i][j-1]) + nums[i][j]
        f[j] = min(f[j], f[j-1]) + nums[i][j]
    分析: 为了避免对i, j取不到的判断, 两种初始化方案:
    解法1:
        这样只初始化第一行, 长度还是N. 95%
    解法2: 
        用N+1避免判断, 而且初始化float('inf')
        但是f[0][0]位置仍然可能是错误的. 所以仍然要判断.
    """
    s = Solution()
    array = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    print(s.minPathSum(array))
