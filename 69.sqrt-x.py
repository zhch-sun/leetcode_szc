#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
class Solution(object):
    # def mySqrt(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     r = x 
    #     while r * r - x > 0:
    #         r = (r + x / r) / 2
    #     return r

    def mySqrt(self, x):
        if x < 2:
            return x
        r = x / 2  # this is Fast
        while r * r - x > 0:
            r = (r + x / r) / 2
        return r

if __name__ == "__main__":
    """
    基础版本是binary search
    牛顿法：
    泰勒展开其实也是牛顿法。。
    牛顿法公式：
    0. x1 = x0 - f(x0)/f'(x0)
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
    print(s.mySqrt(5))
