#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#
class Solution(object):
    # def numTrees(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """        
    #     def dfs(n):
    #         if n == 0:
    #             return 1  # 这里返回1..
    #         if n in used:
    #             return used[n]
    #         ans = 0  # 不是初始化为1...
    #         for i in xrange(0, n):  # Note循环范围
    #             ans += dfs(i) * dfs(n - i - 1)  # 可以只循环一半加速
    #         used[n] = ans
    #         return ans
    #     used = {}
    #     return dfs(n)    

    # def numTrees(self, n):
    #     f = [0] * (n + 1)
    #     f[0] = 1
    #     for i in xrange(1, n + 1):  # 1-based
    #         for j in xrange(i):  # j是左边的个数
    #             f[i] += f[j] * f[i - j - 1]  # 带入i=1得到i-j-1的表达
    #     return f[-1]

    def numTrees(self, n):
        f = [0] * (n + 1)
        f[0] = 1
        for i in xrange(1, n + 1):  # 1-based
            for j in xrange(i // 2):  # j是左边的个数
                f[i] += 2 * f[j] * f[i - j - 1]  # 带入i=1得到i-j-1的表达
            if i & 1:  # 用j & 1 == 0判断偶数
                f[i] += f[i // 2] * f[i // 2]
        return f[-1]

if __name__ == '__main__':
    """
    题设: 不要求平衡树. 多少种BST. 统计个数. 
    解法1: 
        记忆化搜索
        关键在于以某个数为中心的个数等于左右两遍的个数的乘积. 
        对于以j为中心的树, 1~j-1会在左边, j+1~n会在右边. 总共有dp[j-1]*dp[n-j-1]
        dfs时可以记忆化. 注意处理corner case确定循环范围.
    解法2:
        DP. 
    解法3:
        DP优化了中间对称的循环
    解法4:
        数学大法. 求递推公式. 
    """
    s = Solution()
    # print(s.numTrees(5))
    print(s.numTrees(1))
    print(s.numTrees(2))
    print(s.numTrees(3))
