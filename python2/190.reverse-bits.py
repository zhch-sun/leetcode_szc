#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#
class Solution:
    # def reverseBits(self, n):
    # @param n, an integer
    # @return an integer
    #     res = 0
    #     for _ in range(32):
    #         res = (res << 1) & (n & 1 )
    #         n >>= 1
    #     return res

    def reverseBits(self, n):
        """
        """
        # n = n & 0xffffffff # 可以强制32bit
        n = (n >> 16) | (n << 16)  # 16的时候会自动添0所以不用&0x
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

if __name__ == '__main__':
    """
    reverse整数的32bit. 
    解法1: 循环32次. TODO 为什么不能直接在n上搞, 还要额外的res? 
    解法2: 
        类似于mergesort的分治法, 用bit操作来代替循环. 
        abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
    """
    s = Solution()
    print(s.reverseBits(1))
