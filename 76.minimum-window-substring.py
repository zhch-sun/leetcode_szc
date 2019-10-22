#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count, missing = Counter(t), len(t)
        lo, hi = 0, 0  # [lo, hi) 
        rl, rh = 0, float('inf')
        while hi < len(s):
            hi += 1
            if s[hi - 1] in count:  # TODO 这里全是hi-1, 更好表达?
                count[s[hi - 1]] -= 1
                if count[s[hi - 1]] == 0:  # 只在变为0的时刻-1
                    missing -= 1
                while missing == 0:
                    if hi - lo < rh - rl:
                        rh, rl = hi, lo
                    if s[lo] in count:
                        count[s[lo]] += 1
                        if count[s[lo]] >= 0:
                            missing += 1
                    lo += 1
        return '' if rh == float('inf') else s[rl:rh]
        
if __name__ == '__main__':
    """
    题设: 给定字符串S和T, 找到S中包含T的最小窗. 151题是复杂版三指针
    思路: 
        TODO: 这个答案是错的?!
        需要对T进行表示, 因为是只要含有T即可, 所以dict;因为有重复, 所以counter
        需要双指针lo, hi记录当前的窗的位置, 主循环生长hi, 窗运动时修改counter的值
        注意counter不能自动找出当前是否所有均为0, 所以需要一个变量missing辅助记录
        TODO: 能否把missing封装到counter里
        missing为0时可以开始lo的的循环
        中途必须记录res的hi, lo, 因为最后输出的不是大小而是窗
    """
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "aa"))
    print(s.minWindow("aa", "aa"))

