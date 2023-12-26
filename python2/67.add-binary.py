#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """        
        from itertools import izip_longest
        carry = 0
        ans = ''
        for v1, v2 in izip_longest(reversed(a), reversed(b), \
            fillvalue=0):
            carry, val = divmod(int(v1) + int(v2) + carry, 2)
            ans += str(val)
        ans += '1' if carry else ''
        return ans[::-1]

if __name__ == '__main__':
    """
    题设: 两个binary stings相加. 第二题, 445题.
    解法1:
        需要倒序. 以及处理carry!
    """
    s = Solution()
    print(s.addBinary('11', '1'))
    print(s.addBinary('1010', '1011'))
    print(s.addBinary('0', '0'))

