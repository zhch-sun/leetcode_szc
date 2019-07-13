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
        positive = (dividend < 0) == (divisor < 0)  # 必须括号
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:  # >=
            temp, i = b, 1
            while a >= temp:
                a -= temp
                res += i  # 顺序
                temp <<= 1
                i <<= 1

        if not positive:
            return max(-2147483648, -res)  # 2 ** 31
        else:
            return min(2147483647, res) 

if __name__ == '__main__':
    """
    只有一种答案。用减法来做除法。通过右移来实现指数级增加查找范围。
    corner case: 需要处理最大值以及正负。不能直接取abs，因为负数最大值会溢出。
    但是毕竟是python, 所以我直接用long了? 
    另外 -div = 0 - div
    """
    s = Solution()
    print(s.divide(4, 3))
    print(s.divide(5, 3))
    print(s.divide(6, 3))
    print(s.divide(-7, 3))
    print(s.divide(8, 3))
    print(s.divide(10, 3))
    print(s.divide(-37, 3))
    print(s.divide(-2147483648, -1))

