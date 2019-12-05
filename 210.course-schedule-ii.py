#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def dfs(idx):
            memo.add(idx)  # 先加memo!
            onStack.add(idx)
            for j in graph[idx]:
                if j in onStack:
                    return False
                if j not in memo:
                    if not dfs(j):
                        return False
            onStack.remove(idx)
            self.reversePost.append(idx)
            return True

        graph = [[] for _ in xrange(numCourses)]
        for i, j in prerequisites:
            graph[j].append(i)
        memo = set()
        onStack = set()
        self.reversePost = []
        for i in xrange(numCourses):
            if i not in memo:
                if not dfs(i):
                    return []
        return self.reversePost[::-1]

if __name__ == '__main__':
    """
    题设: 只需要返回其中一个解
    解法1: 
        逆后序就是答案. 证明对于任意边v, 调用w时三种情况.
        w已经调用过且返回, w已经被标记, 顺序正确
        w没有调用过, w未来会先返回, 顺序正确
        w已经调用, 未返回: 这是个环. 
    解法2:
        通过入度来搞. 
    """
    s = Solution()
    print(s.findOrder(2, [[1,0]]))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
# @lc code=end

