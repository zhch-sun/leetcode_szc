#
# @lc app=leetcode id=685 lang=python
#
# [685] Redundant Connection II
#

# @lc code=start
class UF(object):
    def __init__(self, N):
        self.fa = list(range(N))

    def find(self, p):
        if self.fa[p] != p:
            self.fa[p] = self.find(self.fa[p])
        return self.fa[p]

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:  # 不能
            return True
        # if qRoot != q:
        #     return [qRoot, q]
        self.fa[qRoot] = pRoot
        return False

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        fa = [0] * (N + 1)
        for e in edges:
            if fa[e[1]] == 0:
                fa[e[1]] = e[0]
            else:
                return [fa[e[1]], e[1]]

        uf = UF(N + 1)
        for e in edges:
            if uf.union(e[0], e[1]):
                return e
        
if __name__ == '__main__':
    """
    有向图, 相比前一道题复杂得多.
        有一个node是所有人的parent.
        两种错误情况: 
        一个node有两个parent.
        存在一个环.
    解法2:
        one-pass. 再UF里面改, 很复杂, 不是直接加一个判断就行
    """
    s = Solution()
    print(s.findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))
    # print(s.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))
    # print(s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))
# @lc code=end

