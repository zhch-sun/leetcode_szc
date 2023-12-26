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
        used = {}
        ans = 0
        lo = 0
        for hi, char in enumerate(s):
            # Note 忘记后面一个判断!!!
            if char not in used or used[char] < lo:  
                ans = max(ans, hi - lo + 1)
            else:
                lo = used[char] + 1
            used[char] = hi
        return ans

    # def lengthOfLongestSubstring(self, s):
    #     from collections import defaultdict
    #     used = defaultdict(int)
    #     ans = 0
    #     lo = 0
    #     for hi, char in enumerate(s):
    #         if char not in used or used[char] == 0:
    #             ans = max(ans, hi - lo + 1)
    #             used[char] += 1
    #         else:
    #             # 额外的while loop
    #             while used[char] > 0:
    #                 used[s[lo]] -= 1
    #                 lo += 1
    #             used[char] += 1
    #     return ans

if __name__ == '__main__':
    """
    题设: 
        找到最长的不存在重复的连续子串
        类似题目209 76
    解法1:
        dict里面记录上一个char的位置.
        可以增加长度的条件: char不存在, 或者!! 位置小于lo!!
    解法2:
        也可以记录数量. 
        只不过遇到重复时要while循环删掉lo后面的字符, 知道删到重复的字符.
    """
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))

