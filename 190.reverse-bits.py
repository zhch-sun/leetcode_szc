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
        Divide and Conquer!  Someway like merge sort.
        For example, if there are 8 bit binary number abcdefgh,
        the process is as follow:
        abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
        """
        n = (n >> 16) | (n << 16) 
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.reverseBits(1))
        

