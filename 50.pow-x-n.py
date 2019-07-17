#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1. / x
            # n = -n  # this will cause overflow if n = INT_MIN
            if n % 2 == 0:
                return self.myPow(x * x, -(n / 2))
            else:
                # Note 注意这里必须n+1,负数的向下取整是另一个方向...
                # Note 括号...
                return x * self.myPow(x * x, -(n / 2 + 1))  
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, n / 2)

if __name__ == '__main__':
    """
    1. 巧妙的拆解方法
    2. 需要处理overflow
    TODO iterative
    """
    s = Solution()
    print(s.myPow(2, -3), 2 ** -3)

