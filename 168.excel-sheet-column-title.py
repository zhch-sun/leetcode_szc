#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n > 0:
            n, remainder = divmod(n - 1, 26)  # quotient remainder
            res.append(chr(remainder + ord('A')))
        return ''.join(res[::-1])
        
if __name__ == '__main__':
    """
    10进制 -> 26进制. 问题是这个26进制没有0... 非常tricky. 见如下链接.
    https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation
    """
    s = Solution()
    print(s.convertToTitle(28))
