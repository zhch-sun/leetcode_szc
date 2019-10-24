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
            res.append(chr(remainder + ord('A')))  # 第一个余数是最低位!
        return ''.join(res[::-1])
        
if __name__ == '__main__':
    """
    题设: 给定一个正整数，返回它在 Excel 表中相对应的列名称 1->A 27->AA
    解法: 
        10进制 -> 26进制. 问题是这个26进制没有0... 非常tricky. 见如下链接.
        https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation
        我的解释: 确定Z和ZZ都对即可. ZZ是26*26+26. 从Z可以推导简单思路:
        Z只能有一位(一次循环即停止), 所以n-1. 这时其他就自然都对了...
        chr函数: ord函数的逆, 给定数字, 返回str
    """
    s = Solution()
    print(s.convertToTitle(28))
