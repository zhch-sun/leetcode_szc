#
# @lc app=leetcode id=903 lang=python
#
# [903] Valid Permutations for DI Sequence
#

# @lc code=start
class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        def dfs(i, j):
            if (not 0 <= j <= N - i) or i < 0:  # 循环变量的范围!
                return 0
            if i == 0:
                return 1  # 这里是初始化!
            if (i, j) in f:
                return f[i, j]
            if S[i - 1] == 'I':
                f[i, j] = dfs(i - 1, j) + dfs(i, j - 1)
            else:
                f[i, j] = dfs(i - 1, j + 1) + dfs(i, j + 1)
            return f[i, j]

        MOD = 10**9 + 7
        N = len(S)
        f = {}
        return dfs(N, 0) % MOD

if __name__ == '__main__':
    """
    解法1:
        https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168278/C%2B%2BJavaPython-DP-Solution-O(N2)
        仔细想清楚可以帮助理解DP. 
        理解什么是集合, 以及状态设计是如何代表集合中的一类数的. 
        基础思路:
            i是index
            已知前i-1个位置的方案数, 求i个位置时的方案数. 然而信息不够.
            i时, 前面i个数, 后面n-i个数, 但是不知道后面是哪些数. 所以需要状态表示
            因为DI只与最后一个数有关, 最后一个数也需要一个状态, 
            合并两个状态, 表示f[i]最后一位在j加上剩下的(N-i)个数的rank, 即第几小. 
            即插入到剩下的数中, 形成一个分割, 需要自己列出来
            例如 DID, 理解里面的连线, 是前缀和.
            f[0,0]=1 (0) f[1,0]=3 (30,20,10) f[2,0]=3 (102,201,301)
            f[0,1]=1 (1) f[1,1]=2 (31,21)    f[2,1]=5 (302,203,103,312,213)
            f[0,2]=1 (2) f[1,2]=1 (32)
            f[0,3]=1 (3) 没有f[1,3]

            if "I"
            f[i][j] = f[i-1][j] + f[i-1][j-1] +.. + f[i-1][0]
            f[i][j-1] =           f[i-1][j-1] +.. + f[i-1][0]            
            f[i][j] = f[i-1][j] + f[i][j-1]
            # f[j] += f[j-1]  # 每次dp的长度需要减1, 是个psum.

            if 'D", 这时i-1的j要大于i的j
            f[i][j]   = f[i-1][j+1] + f[i-1][j+2] + f[i-1][N-i]
            f[i][j+1] =               f[i-1][j+2] + f[i-1][N-i]
            f[i][j]   = f[i-1][j+1] + f[i][j+1]  # 不能直接优化.. 需要另外一个变量

            递推仍然比较复杂, 还是写记忆化搜索好了.
            我这道题和官方solu以及链接中的推导都不一样.

    """
    s = Solution()
    print(s.numPermsDISequence("DID"))     
# @lc code=end

