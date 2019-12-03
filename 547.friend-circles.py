#
# @lc app=leetcode id=547 lang=python
#
# [547] Friend Circles
#

# @lc code=start
class UF(object):
    def __init__(self, N):
        self.fa = list(range(N))  # father node
        self.cnt = N

    def find(self, p):
        # while self.id[p] != p:  # naive实现
        #     p = self.id[p]
        if self.fa[p] != p:  # 直连根节点
            self.fa[p] = self.find(self.fa[p])  # Note fa[p]
        return self.fa[p]

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        self.fa[pRoot] = qRoot  # 连得是root!
        self.cnt -= 1

    def count(self):
        return self.cnt

class Solution(object):
    # def findCircleNum(self, M):
    #     """
    #     :type M: List[List[int]]
    #     :rtype: int
    #     """
    #     N = len(M)
    #     uf = UF(N)
    #     for i in xrange(N):
    #         for j in xrange(i + 1, N):  # 上三角
    #             if M[i][j]:
    #                 uf.union(i, j)
    #     return uf.count()

    def findCircleNum(self, M):
        def dfs(i):
            used[i] = True
            for j in xrange(N):  # 不能上三角..
                if M[i][j] and not used[j]:
                    dfs(j)
                
        N = len(M)
        used = [False] * N
        cnt = 0
        for i in xrange(N):
            if not used[i]:
                dfs(i)
                cnt += 1  # Note 在if内部!!
        return cnt

if __name__ == '__main__':
    """
    题设: 矩阵表示, 返回联通分量的个数. 
    解法1: 并查集
        naive 376ms
        路径压缩 208ms
        搜索上三角矩阵 188ms
    解法2: DFS
        注意不能上三角, 因为dfs的路径可能是奇怪的路径..
    解法3: BFS
        最快, 未写. 用queue或者stack. 
    """
    s = Solution()
    M = [[1,1,0],
        [1,1,0],
        [0,0,1]]
    print(s.findCircleNum(M))
    M = [[1,1,0],
        [1,1,1],
        [0,1,1]] 
    print(s.findCircleNum(M))      
    M = [[1,0,0,1],
         [0,1,1,0],
         [0,1,1,1],
         [1,0,1,1]]        
    print(s.findCircleNum(M))      
# @lc code=end

