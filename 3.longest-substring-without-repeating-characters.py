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
    this problem has many pitfalls. 
    1. I need to keep the start instead of the previous maxLength. 
    2. The condition to renew the start is not just char in map. 
    3. enumerate is better than array indexing in terms of time.
    4. use (item in map) instead of (item in map.keys)
    5. do not use map as variable name!
    """
    s = Solution()
    res = s.lengthOfLongestSubstring('abcabcbb')
    print(res)

