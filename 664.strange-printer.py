#
# @lc app=leetcode id=664 lang=python
#
# [664] Strange Printer
#

# @lc code=start
import itertools
class Solution(object):
    # def strangePrinter(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     # 还是写错了...  下面的link似乎是顺序写最好的写法. 
    #     # https://leetcode.com/problems/strange-printer/discuss/106810/Java-O(n3)-DP-Solution-with-Explanation-and-Simple-Optimization/342701
    #     N = len(s)
    #     # 注意不能 N + 1
    #     f = [[0 for __ in xrange(N)] for _ in xrange(N)]
    #     for n in xrange(1, N + 1):  # [i, j], 即i可以等于j
    #         for i in xrange(N - n):
    #             j = i + n - 1
    #             f[i][j] = f[i + 1][j] + 1
    #             for k in xrange(i + 1, j + 1):
    #                 if s[k] == s[i]:
    #                     f[i][j] = min(f[i][j], f[i][k-1] + f[k+1][j])
    #     return f[0][-1]

    def strangePrinter(self, s):
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) not in memo:  # Note 必须加括号. 
                ans = dp(i + 1, j) + 1
                for k in xrange(i + 1, j + 1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k - 1) + dp(k + 1, j))
                memo[i, j] = ans  # Note 忘记了.. 而且不必括号
            return memo[i, j]  # 不能返回ans. 可能没有赋值
        memo = {}
        s = [k for k, _ in itertools.groupby(s)]
        return dp(0, len(s) - 1)   

if __name__ == '__main__':
    """
    题设: 只能连续打印某个字符, 每次打印覆盖之前, 最小需要多少次打印
    解法1:
        区间DP. 递归搜索. 
        dict memo的速度要比list快很多: 稀疏问题还是dict好得多.
            状态: f[i, j] 表示所有i, j之间的打印方法, 属性是最小值. 
            状态转移: f[i, j], 现在left是i, 考虑此时右边界的位置. 为什么一定这样?  
                只染i位置: f[i + 1][j] + 1
                染到k位置: f[i][k - 1] + f[k+1][j]   (k一定和l颜色相同) 
                而且每次右边沿一定是最终的颜色, 可以反证
            初始化: 0初始化
            返回值: f[0, -1]  # 这里错了...
        循环过程不是对i, j循环, 外环是n, 内环是i, r是i+n. 
    解法2: 
        区间DP, 顺序搜索. 
    """
    s = Solution()
    # print(s.strangePrinter('aaabbb'))
    # print(s.strangePrinter('aba'))
    print(s.strangePrinter('baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa'))
# @lc code=end

