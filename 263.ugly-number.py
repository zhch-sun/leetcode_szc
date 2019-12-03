#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        prime = (2, 3, 5)
        for p in prime:
            while num % p == 0:
                num //= p
        return num == 1
        
if __name__ == '__main__':
    """
    坑:  <= 0!
    """
    s = Solution()
    print(s.isUgly(6))
    print(s.isUgly(8))
    print(s.isUgly(14))
# @lc code=end

