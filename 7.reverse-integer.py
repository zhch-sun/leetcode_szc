#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
class Solution(object):
    # def reverse(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     s = 1 if x >= 0 else -1
    #     r = int(str(s * x)[::-1])
    #     res = r * s
    #     return res if res.bit_length() < 32 or r == -2**31 else 0

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        s = 1 if x >= 0 else -1
        x *= s
        while x != 0:
            res = res * 10 + x % 10
            x /= 10
            if res > 2 ** 31 - 1 or res < -1 * 2 ** 31:
                return 0
        res *= s
        return res


if __name__ == '__main__':
    """
    convert int to string
    Int in python can automatically switch to Long or larger, 
    so we cannot use overflow as a condition to return unlike c or java. 
    And consider the corner cases!! 2**31 and -2**31
    """
    s = Solution()
    print(s.reverse(-123))    

        

