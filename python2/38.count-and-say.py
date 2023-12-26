#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#

import re

class Solution(object):
    # def countAndSay(self, n):
    #     """
    #     :type n: int
    #     :rtype: str
    #     """    
    #     # 单指针, 用cnt, 非常丑. 没法处理最后的特例.
    #     s = '1'
    #     for _ in xrange(n - 1):  # Note n-1
    #         cnt = 1
    #         ns = ''  # next str
    #         for i in xrange(1, len(s)):
    #             if s[i - 1] == s[i]:
    #                 cnt += 1
    #             else:
    #                 ns += str(cnt)
    #                 ns += s[i - 1]
    #                 cnt = 1  # 忘记..
    #         ns += str(cnt)  # 最后忘记...
    #         ns += s[-1]
    #         s = ns
    #     return s

    def countAndSay(self, n):
        # 双指针, 循环lo
        s = '1'
        for _ in xrange(n - 1):  # Note n - 1
            ns = ''
            N = len(s)
            lo = 0
            while lo < N:
                hi = lo + 1
                while hi < N and s[hi] == s[lo]:
                    hi += 1
                ns += str(hi - lo)
                ns += s[lo]
                lo = hi
            s = ns
        return s

    # def countAndSay(self, n):
    #     from itertools import groupby
    #     s = '1'
    #     for _ in xrange(n - 1):  # Note list(g)!
    #         s = ''.join([str(len(list(g))) + k for k, g in groupby(s)])
    #     return s

    # def countAndSay(self, n):
    #     s = '1'
    #     for _ in range(n - 1):
    #         s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    #     return s


if __name__ == '__main__':
    """
    分析: 实际就是写一个groupby. 
    解法1:
        单指针用cnt. 必须单独处理最后一块...
    解法2: 标准解法
        双指针, while loop. 标准解法
    解法3:
        itertools.groupby solution.
    解法4: 
        regular expression results...
    """
    # import itertools
    s = Solution()
    for i in range(10):
        print(s.countAndSay(i+1))
