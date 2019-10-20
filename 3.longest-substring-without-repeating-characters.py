#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        usedChar = dict()
        maxLength = start = 0
        for idx, item in enumerate(s):
            if item in usedChar and start <= usedChar[item]:
                start = usedChar[item] + 1
            else:
                maxLength = max(maxLength, idx - start + 1)
            usedChar[item] = idx
            
        return maxLength


if __name__ == '__main__':
    """
    总体思路：
        需要map, maxlength, start三个变量。
        map存的是每个item的最近出现位置，start是当前的开始位置
        每个循环都要更新三个变量：注意代码里更新位置
    判断条件：
        item是否在map里，item的位置是否小于等于start（注意等于时的操作）
        即使item在map里，但是start大于，则依旧要更新maxLength
        最后在if外面更新map
    many pitfalls. 
    1. The condition to renew the start is not just char in map. 
    2. enumerate is better than array indexing in terms of time???
    3. use (item in map) instead of (item in map.keys)
    4. do not use map as variable name!
    """
    s = Solution()
    res = s.lengthOfLongestSubstring('abcabcbb')
    print(res)

