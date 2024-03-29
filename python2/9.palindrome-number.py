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
            x = (x % ranger) / 10  # 这一步需要掌握
            ranger /= 100  # 这里有个坑
        
        return True
        
if __name__ == '__main__':
    """
    不能用bit_length()，因为是十进制的回文。
    convert to str is easy but involve extra memory
    needs to do without convert to str. Also pitfalls about bit manipulation.
    """
    s = Solution()
    print(s.isPalindrome(-1001))
