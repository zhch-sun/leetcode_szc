#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#
class Solution(object):
    # def titleToNumber(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     num = 0
    #     for char in s:
    #         num *= 26
    #         num += ord(char) - ord('A') + 1
    #     return num

    def titleToNumber(self, s):
        return reduce(lambda x, y: x * 26 + y, [ord(i) - 64 for i in s])

if __name__ == '__main__':
    """
    题设: 给定列名称, 返回序号 z->26 ZZ->26*26+26
    解法: reduce还是不太会用. 从高到底搞. 每个乘以26. 
    """
    s = Solution()
    print(s.titleToNumber('ZY'))
