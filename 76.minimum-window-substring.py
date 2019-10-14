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
        lo, hi = 0, 0
        rl, rh = 0, float('inf')
        while hi < len(s):
            hi += 1
            if s[hi - 1] in count:
                count[s[hi - 1]] -= 1 
                if count[s[hi - 1]] == 0:
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
    用双指针和counter.
    t不是unique的, 如t='aa', window里需要两个a. 
    所以不是一个空的couter, 而是用t初始化counter.
    count的问题是减到0之后相应的key仍然存在, 所以没法直接比较count.keys的长度.
    """
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "aa"))
    print(s.minWindow("aa", "aa"))

