#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 1 if x >= 0 else -1
        r = int(str(s * x)[::-1])
        res = r * s
        return res if res.bit_length() < 32 or r == -2**31 else 0

if __name__ == '__main__':
    """
    convert int to string
    And consider the corner cases!! 2**31 and -2**31
    """
    s = Solution()
    print(s.reverse(1563847412))    

        

