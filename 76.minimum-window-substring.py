#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

from collections import Counter
from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        cnt, missing = Counter(t), len(t)
        lo = 0
        rl, rh = -1, len(s) + 1
        for hi, char in enumerate(s, start=1):  # [lo, hi)
            if char in cnt:  # 可以不加这个判断, 加上逻辑更清晰.
                cnt[char] -= 1
                if cnt[char] >= 0:
                    missing -= 1
                while missing == 0:
                    if hi - lo < rh - rl:
                        rl, rh = lo, hi
                    if s[lo] in cnt:
                        cnt[s[lo]] += 1
                        if cnt[s[lo]] > 0:
                            missing += 1
                    lo += 1  # Note 这个位置不在if里面!
        return s[rl:rh] if rl != -1 else ''

if __name__ == '__main__':
    """
    题设: 
        给定字符串S和T, 找到S中包含T的最小窗. 
        209题是简单版, 只需要求和即可. 
        151题是复杂版 三指针
    解法1: 
        连续子区间: 双指针, 主循环生长hi, 窗运动时修改counter的值
        counter比较复杂: 
            1. 允许负数: 否则lo生长时没法正确恢复
            2. 需要missing变量表示窗内有几个值小于等于0, 否则要额外循环
            3. missing是len(t), 而不是字符的个数
        坑:
            1. 要判断char是否在T里
            2. lo + 1的位置在if外..
        更新rl rh的语句可以放到while循环结束之后(需要while前面再套一层if)
        注意python里 Counter比defaultdict慢了很多. 
    解法2:
        针对S中存在大量T中不存在的字符, 先过滤一遍S, 存下(idx, char) pair
    """
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "aa"))
    print(s.minWindow("aa", "aa"))

