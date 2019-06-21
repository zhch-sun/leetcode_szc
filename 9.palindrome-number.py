#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

class Solution(object):
    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     """
    #     s = str(x)
    #     return s == s[::-1]

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        ranger = 1
        while x // ranger >= 10:
            ranger *= 10

        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            x = (x % ranger) / 10
            ranger /= 100
        
        return True

        
if __name__ == '__main__':
    """
    convert to str is easy but involve extra memory
    needs to do without convert to str. Also pitfalls about bit manipulation.
    """
    s = Solution()
    print(s.isPalindrome(-1001))
