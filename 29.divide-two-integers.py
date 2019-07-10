#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

if __name__ == '__main__':
    """
    只有一种答案。
    需要处理最大值以及正负。不能直接取abs，因为负数最大值会溢出。
    另外 -div = 0 - div
    用减法来做除法。通过右移来实现指数级增加查找范围。
    """
    s = Solution()
       

