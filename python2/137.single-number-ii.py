#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 99.9
        stotal = sum(set(nums)) * 3
        return (stotal - sum(nums)) // 2

if __name__ == '__main__':
    """
    题设: 除了一个出现一次, 其余均出现三次
    解法1: 数学大法.
    解法2: 逻辑电路设计: 设计一个不考虑进位的三进制加法器. 先不写了. 
    """
    s = Solution()
    print(s.singleNumber([2,2,3,2]))
    print(s.singleNumber([0,1,0,1,0,1,99]))

