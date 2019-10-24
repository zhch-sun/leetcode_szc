#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#
class Solution(object):
    # def trailingZeroes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     return 0 if n < 5 else n / 5 + self.trailingZeroes(n / 5)
        
    def trailingZeroes(self, n):
        count = 0
        while n >= 5:
            n /= 5
            count += n
        return count

if __name__ == '__main__':
    """
    题设: 给定一个整数 n，返回 n! 结果尾数中零的数量。
    解法: 
        其实就是计算5的格数(2的个数一定满足) 但是25里面有两个5. 
        第一个除以五是判断能被5整除的数:
        所以再除以5看多少个能被25整除, 然后125... 直到n<5
    """
    s = Solution()
