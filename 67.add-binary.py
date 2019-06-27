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
        l1 = len(a)
        l2 = len(b)
        carry = 0
        res = []
        while l1 or l2 or carry:
            sum = carry
            sum += int(a[l1 - 1]) if l1 > 0 else 0
            sum += int(b[l2 - 1]) if l2 > 0 else 0

            carry, val = divmod(sum, 2)
            l1 -= 1 if l1 > 0 else 0
            l2 -= 1 if l2 > 0 else 0
            res.append(str(val))
        return ''.join(res[::-1])

if __name__ == '__main__':
    """
    和第二题一样呀。。
    Note 循环中 str += 很慢呀
    """
    s = Solution()
    print(s.addBinary('11', '1'))

