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
    #     # 不写了
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
        # 最开始的写法居然是历史最快. 
        def dfs(i, j):  # [i, j]
            if i > j:
                return 0
            if (i, j) in f:  # Note 必须加括号
                return f[i, j]
            ans = dfs(i + 1, j) + 1
            for k in xrange(i + 1, j + 1):
                if s[k] == s[i]:
                    ans = min(ans, dfs(i, k - 1) + dfs(k + 1, j))
            f[i, j] = ans  # Note 忘记了.. 而且不必括号
            return f[i, j]
        f = {}
        s = [k for k, _ in itertools.groupby(s)]  # 主要是这个优化快
        return dfs(0, len(s) - 1)

if __name__ == '__main__':
    """
    题设: 只能连续打印某个字符, 每次打印覆盖之前, 最小需要多少次打印
    解法1: 历史最快!
        区间DP. 与546同样思路. 对i分类讨论, 
            1种是只染自己, f[i + 1][j] + 1
            如果要连续染, 则停下的位置必然是同样颜色. 所以我们穷举停下的位置
            此时f[i][k - 1] + f[k+1][j]
            注意不能f[i + 1][k - 1] + f[k+1][j] + 1, 即去掉首尾加一次
            因为尽管确定了开始位置, 但是中间可能还有和i相同的颜色, 被一起消灭
        dict memo的速度要比list快很多: 稀疏问题还是dict好得多.
        循环过程不是对i, j循环, 外环是n, 内环是i, r是i+n. 
    解法2: 
        DP写法不需要, 因为可以pruning. 
    """
    s = Solution()
    print(s.strangePrinter('aaabbb'))
    print(s.strangePrinter('aba'))
    print(s.strangePrinter('baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa'))
# @lc code=end

