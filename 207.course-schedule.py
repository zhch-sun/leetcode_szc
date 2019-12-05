#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):
    # def canFinish(self, numCourses, prerequisites):
    #     """
    #     :type numCourses: int
    #     :type prerequisites: List[List[int]]
    #     :rtype: bool
    #     """
    #     def dfs(idx):
    #         onStack.add(idx)
    #         memo.add(idx)
    #         for j in graph[idx]:
    #             if j in onStack:
    #                 return False
    #             if j not in memo:
    #                 if not dfs(j):
    #                     return False
    #         onStack.remove(idx)
    #         return True

    #     graph = [[] for _ in xrange(numCourses)]
    #     for i, j in prerequisites:
    #         graph[j].append(i)  # Note忘记append
    #     onStack = set()
    #     memo = set()
    #     for i in xrange(numCourses):
    #         if i not in memo:
    #             if not dfs(i):
    #                 return False
    #     return True
        
    def canFinish(self, numCourses, prerequisites):
        def dfs(idx):  
            memo[idx] = -1
            for j in graph[idx]:
                if memo[j] == -1:
                    return False
                if memo[j] == 0:
                    if not dfs(j):
                        return False
            memo[idx] = 1
            return True

        graph = [[] for _ in xrange(numCourses)]
        memo = [0] * numCourses
        for i, j in prerequisites:
            graph[j].append(i)  # Note 忘记appedn..
        for i in xrange(numCourses):
            if not memo[i]:
                if not dfs(i):
                    return False
        return True

if __name__ == '__main__':
    """
    题设: 问是否可行, 即找环
    解法1:
        首先用邻接表来构建graph
        抄算法数上的方法. 和无环图cycle检测差不多.
    解法2:
        也可以用array, 然后相应位置赋值-1 1表示
        是否见过, 或者onstack
    """
    s = Solution()
    print(s.canFinish(2, [[1,0]]))  # 1是前置要求
    print(s.canFinish(2, [[1,0],[0,1]]))
# @lc code=end

