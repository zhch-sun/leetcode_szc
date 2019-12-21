#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#
class Solution(object):
    # def myPow(self, x, n):
    #     """
    #     :type x: float
    #     :type n: int
    #     :rtype: float
    #     """        
    #     isNeg = n < 0
    #     n = abs(n)
    #     ans = 1  # Note 不能ans=x..
    #     for _ in xrange(n):
    #         ans *= x
    #     return ans if not isNeg else 1. / ans  # float!

    def myPow(self, x, n):
        isNeg = n < 0
        n = abs(n)
        ans = 1
        while n > 0:
            if n & 1:
                ans *= x
            n >>= 1
            x = x * x  # 只是算x,没有更新到n
        return ans if not isNeg else 1. / ans

if __name__ == '__main__':
    """
    题设: 浮点x, 正数n, pow
    解法1:
        for循环. 乘n次. 注意ans初始化为1, 处理n=0的情况..
        TLE了...
    解法2:
        bit迭代: https://leetcode.com/problems/powx-n/discuss/19563/Iterative-Log(N)-solution-with-Clear-Explanation
        N = 9 = 2^3 + 2^0 = 1001
        x^9 = x^(2^3) * x^(2^0)
        循环中:
            算出 x^1, x^2, x^3, x^2
            遇到bit是1的位置, 就把当前的x^n乘到ans里.
    解法3:
        递归太丑了. 删掉. 
    """
    s = Solution()
    print(s.myPow(2, -3), 2 ** -3)
