#
# @lc app=leetcode id=407 lang=python
#
# [407] Trapping Rain Water II
#

# @lc code=start
import heapq    

class Solution(object):
    def trapRainWater(self, grid):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        M, N = len(grid), len(grid[0])
        visited = [[0] * N for _ in xrange(M)]
        hq = []

        # Push 4 borders into heap
        for i in (0, M - 1):
            for j in xrange(N):
                heapq.heappush(hq, (grid[i][j], i, j))
                visited[i][j] = 1
        for i in xrange(1, M - 1):
            for j in (0, N -1):
                heapq.heappush(hq, (grid[i][j], i, j))
                visited[i][j] = 1
        
        result = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while hq:
            height, i, j = heapq.heappop(hq)    
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj]:
                    result += max(0, height-grid[ni][nj])
                    heapq.heappush(hq, (max(grid[ni][nj], height), ni, nj))
                    visited[ni][nj] = 1
        return result        

if __name__ == '__main__':
    """
    神奇的解法. 非边界元素被push进去之后确实不会再长高.
    https://blog.csdn.net/asmartkiller/article/details/97375220
    https://leetcode.com/problems/trapping-rain-water-ii/discuss/89466/python-solution-with-heap
    """
    s = Solution()
    grid = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 
    print(s.trapRainWater(grid))
# @lc code=end

