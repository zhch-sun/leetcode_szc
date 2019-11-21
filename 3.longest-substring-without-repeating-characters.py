#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     usedChar = dict()
    #     maxLength = start = 0
    #     for idx, item in enumerate(s):
    #         if item in usedChar and start <= usedChar[item]:
    #             start = usedChar[item] + 1
    #         else:
    #             maxLength = max(maxLength, idx - start + 1)
    #         usedChar[item] = idx
            
    #     return maxLength

    def lengthOfLongestSubstring(self, s):
        used = {}
        lo = 0
        maxLen = 0
        for hi, char in enumerate(s, start=1):  # [lo,hi)
            if char not in used or used[char] < lo:
                maxLen = max(maxLen, hi - lo)
            else:
                lo = used[char] + 1
            used[char] = hi - 1
        return maxLen

if __name__ == '__main__':
    """
    题设: 找到最长的不存在重复的连续子串
    总体思路：
        类似题目209 76. 不能counter或者set. 
        TODO: 
            大雪菜也给出了counter做法, 就是当当前位置重复时, 
            lo一直递增到当前位置不重复!! 这样依旧是单调的. 
        因为当重复出现时不能lo+1, 而是要知道重复char的位置. 
        所以只能一个dict存位置.
    判断条件：
        item是否在map里，item的位置是否小于等于start（注意等于时的操作）
        即使item在map里，但是start大于，则依旧要更新maxLength
        最后在if外面更新map
    解法:
        解法1和解法2基本一致. 用解法2的模板
        即先处理正常的情况, 再处理需要重新启动计数的情况
    """
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))

