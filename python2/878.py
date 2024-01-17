from math import lcm, gcd
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # 不找精确数字, 定义f(x)是 小于等于x的神奇数字的个数. 
        # num / a 是区间内整除a的个数, num/b是区间内整除b的个数, 
        # 然后再减去既能整除a, 又能整除b的个数
        MOD = 10**9 + 7
        lo, hi = 1, n * max(a, b)  # 范围还可以优化
        c = lcm(a, b)
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = mid // a + mid // b - mid // c  # 容斥原理
            if cnt < n:
                lo = mid + 1
            else:
                hi = mid
        return lo % MOD  # 居然是最后MOD
            