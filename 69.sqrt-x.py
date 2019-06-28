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
    #     r = x 
    #     while r * r - x > 0:
    #         r = (r + x / r) / 2
    #     return r

    # def mySqrt(self, x):
    #     if x < 2:
    #         return x
    #     r = x / 2  # this is Fast, but leads to corner case
    #     while r * r - x > 0:
    #         r = (r + x / r) / 2
    #     return r

    def mySqrt(self, x):
        if x < 2:
            return x        
        left = 0
        right = x / 2
        while left < right:
            # we want solution >= left, need upper bound
            # mid = left + int(math.ceil(float(right - left) / 2))  
            # mid = left + (right - left + 1) / 2  # still overflow
            # https://stackoverflow.com/questions/14822184/is-there-a-ceiling-equivalent-of-operator-in-python
            mid = left + ((right - left) / -2) * -1  # tricks for
            cur = mid * mid - x
            if cur < 0:
                left = mid  # no plus 1
            elif cur > 0:
                right = mid - 1  # must minus 1
            else:
                return mid
        return left
                

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
    print(s.mySqrt(9))
    print(s.mySqrt(11))
