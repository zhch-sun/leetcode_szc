#
# @lc app=leetcode id=299 lang=python
#
# [299] Bulls and Cows
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cntA = 0
        cntB = 0
        d1, d2 = defaultdict(int), defaultdict(int)
        for s1, s2 in zip(secret, guess):
            if s1 == s2:
                cntA += 1
            else:
                d1[s1] += 1
                d2[s2] += 1
        if len(d1) > len(d2):
            d1, d2 = d2, d1
        for k, v in d1.items():
            if k in d2:
                cntB += min(v, d2[k])
        return str(cntA) + 'A' + str(cntB) + 'B'
        
if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.getHint('1807', '7810'))
    print(s.getHint('1123', '0111'))
# @lc code=end

