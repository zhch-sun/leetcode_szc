#
# @lc app=leetcode id=684 lang=python
#
# [684] Redundant Connection
#

# @lc code=start
class UF(object):
    def __init__(self, N):
        self.fa = list(range(N))
    
    def find(self, p):
        if self.fa[p] != p:
            self.fa[p] = self.find(self.fa[p])  # Note fa[p]!
        return self.fa[p]

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return True
        self.fa[pRoot] = qRoot
        return False
        
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        uf = UF(N + 1)  # 输入是1-based
        for e in edges:
            if uf.union(e[0], e[1]):
                return e
        
if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
    print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
# @lc code=end

