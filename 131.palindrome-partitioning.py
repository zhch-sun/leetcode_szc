#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        tmp = []
        self.backtrack(res, tmp, s, 0)
        return res

    def backtrack(self, res, tmp, s, pos):
        for i in range(pos, len(s)):
            item = s[i]
            tmp.append(item)
            self.backtrack(res, tmp, s, i + 1)
            tmp.pop()
    
    def isPal(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
        return True
        
if __name__ == '__main__':
    """
    是个dfs, 并不是backtrack. 
    """
    s = Solution()
