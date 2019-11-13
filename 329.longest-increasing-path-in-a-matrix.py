#
# @lc app=leetcode id=329 lang=python
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if f[i][j] > 0:
                return f[i][j]
            dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
            ans = 1  # 初始化还是错了....
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < M and 0 <= nj < N and nums[ni][nj] > nums[i][j]:
                    ans = max(ans, dfs(ni, nj) + 1)
            f[i][j] = ans
            return ans

        nums = matrix
        if not nums or not nums[0]:
            return 0
        M, N = len(nums), len(nums[0])
        f = [[0] * N for _ in xrange(M)]
        res = 0
        for i in xrange(M):
            for j in xrange(N):
                res = max(res, dfs(i, j))
        return res  # max([max(n) for n in f]) max matrix的写法..
        
if __name__ == '__main__':
    """
    
    """
    s = Solution()
    # matrix = [
    # [9,9,4],
    # [6,6,8],
    # [2,1,1]
    # ] 
    matrix = [
    [3,4,5],
    [3,2,6],
    [2,2,1]
    ] 
    matrix = [[1,2]]
    matrix = [
    [7,7,5],
    [2,4,6],
    [8,2,0]
    ] 
    print(s.longestIncreasingPath(matrix))
# @lc code=end

