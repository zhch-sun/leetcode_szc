#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

class Solution(object):
    # def uniquePathsWithObstacles(self, obstacleGrid):
    #     """
    #     :type obstacleGrid: List[List[int]]
    #     :rtype: int
    #     """        
    #     # O(n2)空间, 学习循环内写法!!
    #     g = obstacleGrid
    #     if not g or not g[0]:
    #         return None
    #     M, N = len(g), len(g[0])
    #     f = [[0] * N for i in xrange(M)]
    #     f[0][0] = 0 if g[0][0] else 1  # Note 处理[[1]]的情况!!
    #     for i in xrange(M):
    #         for j in xrange(N):
    #             if g[i][j]:
    #                 continue  # 已经初始化为0了
    #             if i:
    #                 f[i][j] += f[i - 1][j]
    #             if j:
    #                 f[i][j] += f[i][j - 1]
    #     return f[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        nums = obstacleGrid
        if not nums or not nums[0]:
            return 0
        M, N = len(nums), len(nums[0])
        f = [0] * N
        f[0] = 0 if nums[0][0] else 1  # 其实不需要判断
        # f[0] = 1
        for i in xrange(M):
            for j in xrange(N):
                if nums[i][j]:
                    f[j] = 0
                elif j > 0:
                    f[j] += f[j - 1]
        return f[-1]

if __name__ == '__main__':
    """
    解法1:
        原始dp解法. O(N2)空间. 
        注意初始化! 其实不需要提供一个判断, 但是最好还是考虑. 
    解法2:
        O(N)空间    
    """
    s = Solution()
    array = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
            ] 
    # array = [[0], [1]]
    print(s.uniquePathsWithObstacles(array))
