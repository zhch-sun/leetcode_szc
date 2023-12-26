#
# @lc app=leetcode id=847 lang=python
#
# [847] Shortest Path Visiting All Nodes
#

# @lc code=start
from collections import deque, defaultdict
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        dist = defaultdict(lambda: float('inf'))
        # 初始化所有的起点
        for i in xrange(N):
            dist[1 << i, i] = 0  # 状态压缩
        # 从所有点开始搜索.
        dq = deque([(1 << i, i) for i in xrange(N)]) 
        while dq:
            state, head = dq.popleft()
            d = dist[(state, head)]
            if state == (1 << N) - 1:  # 括号..
                return d
            for j in graph[head]:
                state2 = state | (1 << j)
                if d + 1 < dist[(state2, j)]:
                    dist[(state2, j)] = d + 1
                    dq.append((state2, j))

if __name__ == '__main__':
    """
    解法1:
        不是最小生成树, 因为要有个路径参见例1
        所以也不是最短路.
        所以dict记忆的是, 访问了同样n个节点时, 且同一个head的最小值
        复杂度2^N * N
    解法2:
        DFS思路更清晰. 也更快.
        见submission最快的答案. 
    """
    s = Solution()
    print(s.shortestPathLength([[1,2,3],[0],[0],[0]]))
    print(s.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))
        
# @lc code=end

