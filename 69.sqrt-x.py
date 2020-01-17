#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

import math
class Solution(object):
    # def mySqrt(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """        
    #     lo, hi = 0, x // 2 + 1  # 处理0输入..
    #     while lo < hi:  # [lo, hi]
    #         mid = lo + (hi - lo + 1) // 2  # Note 死循环..
    #         if mid * mid <= x:
    #             lo = mid
    #         else:
    #             hi = mid - 1  # 忘记了.
    #     return lo

    def mySqrt(self, x):
        # 牛顿法
        r = x / 2 + 1
        while r * r - x > 0:
            r = (r + x / r) / 2
        return r

if __name__ == "__main__":
    """
    题设: int sqrt(int x); x > 0, 只返回整数部分.
    解法1:
        二分. 注意处理死循环..
        处理0, 1的corner case.
    解法2:
        牛顿迭代法。设f(x)=x^3-y, 求f(x)=0时的解x，即为y的立方根。        
        没完全理解, 不是对x^0.5求导. 而是对x^2求导
        f(x) = x^2 - N 当f(x)=0的解
        牛顿法(泰勒展开其实也是牛顿法。。)：
        斜率公式 -> 牛顿法公式：
            f'(x0) = f(x0) / (x0 - x1) ->
            x1 = x0 - f(x0)/f'(x0)
        推导方法:
        通过（x0, f(x0)), (x1, 0)两个点。 所以
        0 - f(x0) = (x1 - x0) * f'(x0)
        本题方法:
        1. f(r) = r * r - x 
        2. r(n+1) = r(n) - f(r(n)) / f'(r(n))
        3. r(n+1) = r(n) - (r(n)^2 - x) / 2 * r(n)
        4. r(n+1) = (r(n) + x / r(n)) / 2
    """
    s = Solution()
    print(s.mySqrt(0))
    print(s.mySqrt(1))
    print(s.mySqrt(5))
    print(s.mySqrt(9))
    print(s.mySqrt(11))
