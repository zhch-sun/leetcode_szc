#
# @lc app=leetcode id=72 lang=python
#
# [72] Edit Distance
#

# @lc code=start
class Solution(object):
    # def minDistance(self, word1, word2):
    #     """
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     w1, w2 = word1, word2
    #     M, N = len(w1), len(w2)
    #     f = [[0] * (N + 1) for _ in xrange(M + 1)]
    #     for i in xrange(M + 1):
    #         f[i][0] = i
    #     for j in xrange(N + 1):
    #         f[0][j] = j
        
    #     for i in xrange(M):
    #         for j in xrange(N):
    #             if w1[i] == w2[j]:  # 这种分类讨论更快
    #                 f[i+1][j+1] = f[i][j]
    #             else:
    #                 f[i+1][j+1] = min([f[i+1][j], \
    #                     f[i][j+1], f[i][j]]) + 1                    
    #     return f[-1][-1]

    # def minDistance(self, word1, word2):
    #     # 76ms / 64ms
    #     def dfs(i, j):
    #         if i == 0:
    #             return j
    #         if j == 0:
    #             return i
    #         if f[i][j]:
    #             return f[i][j]

    #         if word1[i - 1] == word2[j - 1]:  # 这里啊....
    #             ans = dfs(i-1, j-1)
    #         else:
    #             ans = min(dfs(i-1, j), \
    #                 dfs(i, j-1), dfs(i-1, j-1)) + 1
    #         f[i][j] = ans  # Note 忘记赋值了...
    #         return ans
            
    #     M, N = len(word1), len(word2)
    #     f = [[0] * (N + 1) for _ in xrange(M + 1)]
    #     return dfs(M, N)
    
    def minDistance(self, word1, word2):
        # 80ms/ 88ms
        def dfs(i, j):
            if i < 0:  # 首先没想到这两个判断..
                return j + 1 # 其次是i+1, 返回的是个数..
            if j < 0:
                return i + 1
            if (i, j) in f:
                return f[i, j]            
            if word1[i] == word2[j]:
                f[i, j] = dfs(i-1, j-1)
            else:
                f[i, j] = min(dfs(i-1,j), dfs(i,j-1), dfs(i-1,j-1)) + 1
            return f[i, j]
             
        M, N = len(word1), len(word2)   # 不需要判断M和N, dfs中判断了.
        f = {}
        return dfs(M - 1, N - 1) 

if __name__ == '__main__':
    """
    题设:
        给两个word, 找到最小操作数使a变成b
        三种操作: 插入, 删除, 替换, 均为任意位置. 
    分析:
        wiki很好. 里面列了最新进展, 有O(max(m,n))的算法
        证明: google "minimum edit distance proof"
        讲解: https://web.stanford.edu/class/cs124/lec/med.pdf
        需要证明为什么先从中间搞不会更快. 还没有时间看. 
    解法1:
        DP是个穷举. 递推中不可能找到最终的解法路径!
        集合: f[i][j]所有将s1中前i个字母, 变成s2中前j个字母的方案.
        属性: 求方案的opt的最小值. 
        状态转移方程: f[i][j] = 
            下面的操作都是针对第i+1个字符.
            空: f[i-1][j-1] 当w1[i]==w2[j]
            替换: f[i-1][j-1] + 1, 当二数不等, 替换第i+1个字符.
            删除: f[i-1][j] + 1, i-1,j早已匹配, i无用, 删除i使i,j匹配
            插入: f[i][j-1] + 1, 在第i个字符后插入新值与j匹配
        注意是已经变成. 所以过程不考虑, 只考虑最后一步!!
        
        alignment: 
            目的: 不仅知道dist, 还要知道操作顺序, 即矩阵图上的线. 
            分析中把空和替换放在一起讲的原因是: 
                二者在矩阵图上都是 对角线 方向.
    解法2: O(m+n). 
        记忆化DP/ backtrace, 直接递归即可. 
        加速原因:
            遇到w1[i]==w2[j]时可以直接转移, 没有分支
            没找到证明 O(m+n) 的证明
    """
    s = Solution()
    print(s.minDistance("horse", "ros"))
    print(s.minDistance("intention", "execution"))
    print(s.minDistance("a", ""))
    
# @lc code=end

