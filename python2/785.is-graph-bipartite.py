#
# @lc app=leetcode id=785 lang=python
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(i):  # i是个没访问过的结点.
            used[i] = True  # 在这里赋值!
            for u in graph[i]: 
                if used[u]:
                    if color[u] == color[i]:
                        return False 
                    continue
                color[u] = ~color[i]
                if not dfs(u):  # Note 忘记dfs了...
                    return False  # 忘记在这里返回..
            return True

        if not graph:
            return True
        N = len(graph)
        used = [False] * N
        color = [False] * N
        for i in xrange(N):
            if not used[i]:
                if not dfs(i):  # 不在这里赋值used[i]
                    return False
        return True

if __name__ == '__main__':
    """
    题设: 
        无向图. 简单图. 
        图用邻接表表示. 0-based
    解法1:
        见算法书. 每个dfs解决一个连通分量
    解法2:
        没写. bfs也可以. 每个bfs解决一个连通分量
    """
    s = Solution()
    print(s.isBipartite([[1,3], [0,2], [1,3], [0,2]]))
    print(s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
    print(s.isBipartite([[2,3,5,6,7,8,9],[2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[1,2,3,6,9],[0,1,2,3,7,8,9],[0,1,2,3,4,7,8,9],[0,1,2,3,5,6,8,9],[0,1,2,3,5,6,7],[0,1,2,3,4,5,6,7]]))
        

# @lc code=end

