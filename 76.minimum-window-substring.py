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
        rl, rh = 0, float('inf')
        for hi, char in enumerate(s, start=1):  # [lo, hi)
            missing -= 1 if cnt[char] > 0 else 0
            cnt[char] -= 1
            while missing == 0:
                # 可以在while外面加一个if判断, 然后把下面的赋值拿出去, 更快                        
                if hi - lo < rh - rl:  
                    rl, rh = lo, hi         
                if s[lo] in cnt:
                    cnt[s[lo]] += 1
                    if cnt[s[lo]] > 0:
                        missing += 1
                lo += 1
        return '' if rh == float('inf') else s[rl:rh]              

if __name__ == '__main__':
    """
    题设: 
        给定字符串S和T, 找到S中包含T的最小窗. 
        209题是简单版, 只需要求和即可. 
        151题是复杂版 三指针
    解法1: 
        1. 需要对T进行表示, 注意Counter比defaultdict慢了很多. 
        2. 需要双指针lo, hi记录当前的窗的位置, 主循环生长hi, 窗运动时修改counter的值
        3. 注意counter不能自动找出当前是否所有均为0, 所以需要一个变量missing辅助记录
        4. 更新rl rh的语句可以放到while循环结束之后(需要while前面再套一层if)
    解法2:
        针对S中存在大量T中不存在的字符, 先过滤一遍S, 存下(idx, char) pair
    """
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "aa"))
    print(s.minWindow("aa", "aa"))

