#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#
class Solution(object):
    # def hammingWeight(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     cnt = 0
    #     for _ in range(32):
    #         cnt += n & 1
    #         n >>= 1
    #     return cnt
        
    def hammingWeight(self, n):
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

if __name__ == '__main__':
    """
    题设: 返回一个无符号整数二进制表达中1的个数. 
    解法1: 32次循环
    解法2: 
        官方solution里有清晰描述. Kernighan's算法, 循环次数与1的个数一样: 
        Each time of "n &= n - 1", we delete one '1' from n.
        n:   110100
        n-1: 110011
        前面不变. 0的部分变1, 最后一个1变0, and之后就消掉一个1. 
    """
    s = Solution()
    print(s.hammingWeight(3))

