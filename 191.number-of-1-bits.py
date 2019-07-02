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
    TODO 快速算法依旧是divide and conquer..
    还有个Kernighan's算法, 循环次数与1的个数一样: 
    Each time of "n &= n - 1", we delete one '1' from n.
    """
    s = Solution()
    print(s.hammingWeight(3))

