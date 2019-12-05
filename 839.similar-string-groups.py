#
# @lc app=leetcode id=839 lang=python
#
# [839] Similar String Groups
#

# @lc code=start
from collections import defaultdict
class UF(object):
    def __init__(self, N):
        self.fa = list(range(N))
        self.count = N

    def find(self, p):
        if self.fa[p] != p:
            self.fa[p] = self.find(self.fa[p])
        return self.fa[p]

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return  
        self.fa[pRoot] = qRoot  # 又忘了..
        self.count -= 1
        
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def similar(s1, s2):
            cnt = 0
            for c1, c2 in zip(s1, s2):
                if c1 == c2:
                    cnt += 1
            return cnt == len(s1) - 2
        N, W = len(A), len(A[0])
        uf = UF(N)
        if N < W * W:
            for i in xrange(N):
                for j in xrange(i + 1, N):
                    if similar(A[i], A[j]):
                        uf.union(i, j)
        else:
            bucket = defaultdict(set)
            for i, word in enumerate(A):
                L = list(word)
                for j in xrange(W):
                    for k in xrange(j + 1, W):
                        L[j], L[k] = L[k], L[j]
                        bucket[''.join(L)].add(i)
                        L[j], L[k] = L[k], L[j]
            for i, word in enumerate(A):
                for j in bucket[word]:
                    uf.union(i, j)
        return uf.count
        
if __name__ == '__main__':
    """
    题设: 是127题word ladder的继续. 
    解法1:
        分段解决. 
        复杂度分析
            1. 暴力法 N2 * w, w是word width
            2. 枚举一个单词所有可能的邻居, N * W3
            所以N > W^2时, 用第二种
            N 最多可以有C(W, W) 8 * 7 * 6 * ... 1
            阶乘的复杂度是超过2^N... 注意啊!!!
        算法: 
            bucket是一个二分图.
    """
    s = Solution()
    # print(s.numSimilarGroups(["tars","rats","arts","star"]))
    # print(s.numSimilarGroups(["blw","bwl","wlb"]))

# @lc code=end

